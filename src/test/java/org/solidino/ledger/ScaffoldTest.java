package org.solidino.ledger;

import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.context.ApplicationContext;

import static org.assertj.core.api.Assertions.assertThat;

@SpringBootTest
class ScaffoldTest {
    @org.springframework.test.context.DynamicPropertySource
    static void testCredential(org.springframework.test.context.DynamicPropertyRegistry properties) {
        properties.add("LEDGER_ADMIN_TOKEN", () -> java.util.UUID.randomUUID().toString());
    }

    @Test
    void startsLedgerContext(@Autowired ApplicationContext context) {
        assertThat(context.getBean(LedgerApplication.class)).isNotNull();
    }
}
