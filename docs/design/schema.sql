-- Stage 2 reference DDL. Each application connection enables foreign keys.
PRAGMA foreign_keys = ON;

CREATE TABLE users (
    id TEXT PRIMARY KEY,
    display_name TEXT NOT NULL CHECK(length(display_name) BETWEEN 1 AND 100),
    token_digest BLOB NOT NULL UNIQUE CHECK(length(token_digest) = 32)
) STRICT;

CREATE TABLE accounts (
    id TEXT PRIMARY KEY,
    owner_id TEXT REFERENCES users(id),
    currency TEXT NOT NULL CHECK(currency IN ('INR','USD','EUR')),
    balance_minor INTEGER NOT NULL DEFAULT 0 CHECK(owner_id IS NULL OR balance_minor >= 0),
    UNIQUE(owner_id, currency),
    UNIQUE(id, currency)
) STRICT;
CREATE UNIQUE INDEX one_clearing_account ON accounts(currency) WHERE owner_id IS NULL;

CREATE TABLE postings (
    sequence INTEGER PRIMARY KEY AUTOINCREMENT,
    id TEXT NOT NULL UNIQUE,
    kind TEXT NOT NULL CHECK(kind IN ('fund','transfer','reversal')),
    currency TEXT NOT NULL CHECK(currency IN ('INR','USD','EUR')),
    amount_minor INTEGER NOT NULL CHECK(amount_minor > 0),
    posted_at TEXT NOT NULL,
    original_id TEXT UNIQUE REFERENCES postings(id),
    digest TEXT NOT NULL CHECK(length(digest) = 64 AND digest NOT GLOB '*[^0-9a-f]*'),
    CHECK((kind = 'reversal') = (original_id IS NOT NULL)),
    CHECK(id IS NOT original_id),
    UNIQUE(id, currency, amount_minor)
) STRICT;
CREATE TABLE entries (
    posting_id TEXT NOT NULL,
    currency TEXT NOT NULL,
    amount_minor INTEGER NOT NULL,
    account_id TEXT NOT NULL,
    side TEXT NOT NULL CHECK(side IN ('debit','credit')),
    PRIMARY KEY(posting_id, side),
    UNIQUE(posting_id, account_id),
    FOREIGN KEY(posting_id, currency, amount_minor) REFERENCES postings(id, currency, amount_minor),
    FOREIGN KEY(account_id, currency) REFERENCES accounts(id, currency)
) STRICT;
CREATE INDEX account_history ON entries(account_id, posting_id);

CREATE TABLE retries (
    caller TEXT NOT NULL,
    operation TEXT NOT NULL,
    retry_key TEXT NOT NULL,
    fingerprint BLOB NOT NULL CHECK(length(fingerprint) = 32),
    posting_id TEXT NOT NULL UNIQUE REFERENCES postings(id),
    status INTEGER NOT NULL CHECK(status = 201),
    response BLOB NOT NULL,
    PRIMARY KEY(caller, operation, retry_key)
) STRICT;
CREATE TRIGGER postings_no_update BEFORE UPDATE ON postings
BEGIN SELECT RAISE(ABORT, 'committed record is immutable'); END;
CREATE TRIGGER postings_no_delete BEFORE DELETE ON postings
BEGIN SELECT RAISE(ABORT, 'committed record is immutable'); END;
CREATE TRIGGER entries_no_update BEFORE UPDATE ON entries
BEGIN SELECT RAISE(ABORT, 'committed record is immutable'); END;
CREATE TRIGGER entries_no_delete BEFORE DELETE ON entries
BEGIN SELECT RAISE(ABORT, 'committed record is immutable'); END;
CREATE TRIGGER retries_no_update BEFORE UPDATE ON retries
BEGIN SELECT RAISE(ABORT, 'committed record is immutable'); END;
CREATE TRIGGER retries_no_delete BEFORE DELETE ON retries
BEGIN SELECT RAISE(ABORT, 'committed record is immutable'); END;
