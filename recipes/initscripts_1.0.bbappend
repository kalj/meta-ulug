FILESEXTRAPATHS:append := ":${THISDIR}/${PN}"
SRC_URI:append = " file://setup-wifi.sh"

do_install:append () {
    install -m 0755    ${WORKDIR}/setup-wifi.sh     ${D}${sysconfdir}/init.d

    update-rc.d -r ${D} setup-wifi.sh start 99 2 3 4 5 .
}

MASKED_SCRIPTS:append = " \
setup-wifi \
"
