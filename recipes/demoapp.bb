DESCRIPTION = "Demo app for ULUG Hack"
SECTION = "examples"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COMMON_LICENSE_DIR}/MIT;md5=0835ade698e0bcf8506ecda2f7b4f302"

FILESEXTRAPATHS:prepend := "${THISDIR}/${PN}:"

SRC_URI = " file://demoapp.py"

do_install () {
    install -m 0755    ${WORKDIR}/demoapp.py     ${D}/
}

RDEPENDS:${PN} = "rpi-gpio python3"

FILES:${PN} = "/"
