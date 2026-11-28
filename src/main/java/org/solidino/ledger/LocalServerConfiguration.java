package org.solidino.ledger;

import java.net.InetAddress;

import org.springframework.boot.web.embedded.tomcat.TomcatServletWebServerFactory;
import org.springframework.boot.web.server.WebServerFactoryCustomizer;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.env.Environment;

@Configuration
class LocalServerConfiguration {
    @Bean
    WebServerFactoryCustomizer<TomcatServletWebServerFactory> localServer(Environment env)
            throws java.net.UnknownHostException {
        String secret = env.getProperty("LEDGER_ADMIN_TOKEN", "");
        if (secret.codePointCount(0, secret.length()) < 16) {
            throw new IllegalStateException("A valid administrator credential is required");
        }
        String host = env.getRequiredProperty("server.address");
        InetAddress address = InetAddress.getByName(host);
        if (host.isBlank() || !address.isLoopbackAddress()) {
            throw new IllegalStateException("A loopback bind address is required");
        }
        return factory -> factory.setAddress(address);
    }
}
