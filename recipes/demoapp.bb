DESCRIPTION = "Demo app for ULUG Hack"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI = "file://demoapp.py \
           file://start-demoapp.sh"

inherit update-rc.d

INITSCRIPT_NAME = "demoapp.sh"
INITSCRIPT_PARAMS = "start 99 2 3 4 5 ."

do_install () {
    install -d ${D}${bindir}
    install -m 0755    ${WORKDIR}/demoapp.py     ${D}${bindir}/
    install -d ${D}${INIT_D_DIR}
    install -m 0755    ${WORKDIR}/start-demoapp.sh     ${D}${INIT_D_DIR}/demoapp.sh
#    update-rc.d -r ${D} demoapp.py start 99 2 3 4 5 .
}

RDEPENDS:${PN} = "rpi-gpio python3"

FILES:${PN} += " ${INIT_D_DIR}/demoapp.sh"
