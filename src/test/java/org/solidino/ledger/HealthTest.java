package org.solidino.ledger;

import org.junit.jupiter.api.Test;
import org.springframework.http.ResponseEntity;

import static org.assertj.core.api.Assertions.assertThat;

class HealthTest {
    @Test
    void respondsWithUncachedJson() {
        ResponseEntity<?> response = new HealthController().health();
        assertThat(response.getHeaders().getCacheControl()).isEqualTo("no-store");
        assertThat(response.getHeaders().getFirst("X-Content-Type-Options")).isEqualTo("nosniff");
        assertThat(response.getBody()).isEqualTo(java.util.Map.of("status", "ok"));
    }
}
