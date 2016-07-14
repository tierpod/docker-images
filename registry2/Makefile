HOST = registry2
CERTS_DIR = certs

ROOTCA_KEY = $(CERTS_DIR)/rootCA.key
ROOTCA_CRT = $(CERTS_DIR)/rootCA.crt
HOST_KEY = $(CERTS_DIR)/$(HOST).key
HOST_CSR = $(CERTS_DIR)/$(HOST).csr
HOST_CRT = $(CERTS_DIR)/$(HOST).crt
SUBJ = /C=RU/L=Location/O=Organization/OU=IT/CN=$(HOST)

.PHONY: all clean rootca host

all: rootca host

rootca: $(ROOTCA_KEY) $(ROOTCA_CRT)

host: $(HOST_KEY) $(HOST_CSR) $(HOST_CRT)

$(CERTS_DIR):
	mkdir $@

$(ROOTCA_KEY): | $(CERTS_DIR)
	openssl genrsa -out $@ 2048

$(ROOTCA_CRT): $(ROOTCA_KEY)
	openssl req -x509 -new -key $(ROOTCA_KEY) -days 3650 -out $@ -subj "$(SUBJ)"

$(HOST_KEY): | $(CERTS_DIR)
	openssl genrsa -out $@ 2048

$(HOST_CSR): $(HOST_KEY)
	openssl req -new -key $(HOST_KEY) -out $@ -subj "$(SUBJ)" -config openssl.cnf

$(HOST_CRT): $(HOST_CSR) $(ROOTCA_CRT) $(ROOTCA_KEY)
	openssl x509 -req -in $(HOST_CSR) -CA $(ROOTCA_CRT) -CAkey $(ROOTCA_KEY) \
		-CAcreateserial -out $@ -days 3650 -extensions v3_req -extfile openssl.cnf

clean:
	rm -r $(CERTS_DIR)

