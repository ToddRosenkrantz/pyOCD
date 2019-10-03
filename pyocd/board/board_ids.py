# pyOCD debugger
# Copyright (c) 2017 Arm Limited
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class BoardInfo(object):
    def __init__(self, name, target, binary):
        self.name = name
        self.target = target
        self.binary = binary

BOARD_ID_TO_INFO = {
  # Note: please keep board list sorted by ID!
  #
  # Board ID            Board Name              Target              Test Binary
    "0200": BoardInfo(  "FRDM-KL25Z",           "kl25z",            "l1_kl25z.bin"          ),
    "0201": BoardInfo(  "FRDM-KW41Z",           "kw41z4",           "l1_kw41z4.bin"         ),
    "0202": BoardInfo(  "USB-KW41Z",            "kw41z4",           "l1_kw41z4.bin"         ),
    "0203": BoardInfo(  "TWR-KL28Z72M",         "kl28z",            "l1_kl28z.bin",         ),
    "0204": BoardInfo(  "FRDM-KL02Z",           "kl02z",            "l1_kl02z.bin",         ),
    "0205": BoardInfo(  "FRDM-KL28Z",           "kl28z",            "l1_kl28z.bin",         ),
    "0206": BoardInfo(  "TWR-KE18F",            "ke18f16",          "l1_ke18f16.bin",       ),
    "0210": BoardInfo(  "FRDM-KL05Z",           "kl05z",            "l1_kl05z.bin",         ),
    "0213": BoardInfo(  "FRDM-KE15Z",           "ke15z7",           "l1_ke15z7.bin",        ),
    "0214": BoardInfo(  "Hexiwear",             "k64f",             "l1_k64f.bin",          ),
    "0215": BoardInfo(  "FRDM-KL28ZEM",         "kl28z",            "l1_kl28z.bin",         ),
    "0216": BoardInfo(  "HVP-KE18F",            "ke18f16",          "l1_ke18f16.bin",       ),
    "0217": BoardInfo(  "FRDM-K82F",            "k82f25615",        "l1_k82f.bin",          ),
    "0218": BoardInfo(  "FRDM-KL82Z",           "kl82z7",           "l1_kl82z.bin",         ),
    "0219": BoardInfo(  "TWR-KV46F150M",        "mkv46f256vll16",   None,                   ),
    "0220": BoardInfo(  "FRDM-KL46Z",           "kl46z",            "l1_kl46z.bin",         ),
    "0221": BoardInfo(  "TWR-KV11Z75M",         "kv11z7",           None,                   ),
    "0222": BoardInfo(  "FRDM-KEA128Z",         "skeaz128xxx4",     None,                   ),
    "0223": BoardInfo(  "FRDM-KE02Z",           "mke02z64vlh4",     None,                   ),
    "0224": BoardInfo(  "FRDM-K28F",            "k28f15",           "l1_k28f.bin",          ),
    "0225": BoardInfo(  "FRDM-K32W042",         "k32w042s",         "l1_k32w042s.bin",      ),
    "0226": BoardInfo(  "MIMXRT1020-EVK",       "mimxrt1020",       "l1_mimxrt1020-evk.bin",),
    "0227": BoardInfo(  "MIMXRT1050-EVKB",      "mimxrt1050_hyperflash", "l1_mimxrt1050-evkb_hyperflash.bin",),
    "0228": BoardInfo(  "Rapid-IoT-K64F",       "k64f",             None,                   ),
    "0230": BoardInfo(  "FRDM-K20D50M",         "k20d50m",          "l1_k20d50m.bin",       ),
    "0231": BoardInfo(  "FRDM-K22F",            "k22f",             "l1_k22f.bin",          ),
    "0232": BoardInfo(  "MIMXRT1064-EVK",       "mimxrt1064cvl5a",  None,                   ),
    "0233": BoardInfo(  "FRDM-KE16Z",           "mke16z64vlf4",     None,                   ),
    "0234": BoardInfo(  "Rapid-IoT-KW41Z",      "kw41z4",           "l1_kw41z4.bin",        ),
    "0235": BoardInfo(  "LPC54018IoTModule",    "lpc54018jet180",   None,                   ),
    "0236": BoardInfo(  "LPCXpresso55S69",      "lpc55s69",         "lpcxpresso55s69.bin",  ),
    "0240": BoardInfo(  "FRDM-K64F",            "k64f",             "l1_k64f.bin",          ),
    "0245": BoardInfo(  "IBMEthernetKit",       "k64f",             "l1_k64f.bin"           ),
    "0250": BoardInfo(  "FRDM-KW24D512",        "kw24d5",           "l1_kw24d5.bin"         ),
    "0251": BoardInfo(  "FRDM-KW36",            "kw36z4",           "l1_kw36z.bin",         ),
    "0260": BoardInfo(  "FRDM-KL26Z",           "kl26z",            "l1_kl26z.bin",         ),
    "0261": BoardInfo(  "FRDM-KL27Z",           "kl27z4",           "l1_kl27z.bin",         ),
    "0262": BoardInfo(  "FRDM-KL43Z",           "kl43z4",           "l1_kl26z.bin",         ),
    "0270": BoardInfo(  "FRDM-KE02Z40M",        "mke02z64vlh4",     None,                   ),
    "0280": BoardInfo(  "TWR-K24F120M",         "mk24fn256vdc12",   None,                   ),
    "0290": BoardInfo(  "FRDM-KW40Z",           "kw40z4",           "l1_kw40z.bin",         ),
    "0291": BoardInfo(  "TWR-KL82Z72M",         "kl82z7",           "l1_kl82z.bin",         ),
    "0298": BoardInfo(  "FRDM-KV10Z",           "kv10z7",           "l1_kl25z.bin"          ),
    "0300": BoardInfo(  "TWR-KV11Z75M",         "kv11z7",           "l1_kl25z.bin"          ),
    "0305": BoardInfo(  "MTS_MDOT_F405RG",      "stm32f405rg",      None                    ),
    "0310": BoardInfo(  "MTS_DRAGONFLY_F411RE", "stm32f411re",      None                    ),
    "0311": BoardInfo(  "FRDM-K66F",            "k66f18",           "l1_k66f.bin",          ),
    "0312": BoardInfo(  "MTS_DRAGONFLY_L471QG", "stm32l471qg",      None                    ),
    "0315": BoardInfo(  "MTS_MDOT_F411RE",      "stm32f411re",      None                    ),
    "0320": BoardInfo(  "FRDM-KW01Z9032",       "kw01z4",           "l1_kl26z.bin"          ),
    "0321": BoardInfo(  "USB-KW01Z",            "kw01z4",           "l1_kl25z.bin"          ),
    "0324": BoardInfo(  "USB-KW40Z",            "kw40z4",           "l1_kl25z.bin"          ),
    "0330": BoardInfo(  "TWR-KV58F220M",        "mkv58f512vll24",   None,                   ),
    "0340": BoardInfo(  "TWR-K80F150M",         "mk80fn256vll15",   None,                   ),
    "0341": BoardInfo(  "FRDM-KV31F",           "mkv31f512vll12",   None,                   ),
    "0350": BoardInfo(  "XDOT_L151CC",          "stm32l151cc",      None                    ),
    "0400": BoardInfo(  "MAXWSNENV",            "max32600",         "l1_maxwsnenv.bin",     ),
    "0405": BoardInfo(  "MAX32600MBED",         "max32600",         "l1_max32600mbed.bin",  ),
    "0406": BoardInfo(  "MAX32620MBED",         "max32620",         None                    ),
    "0407": BoardInfo(  "MAX32620HSP",          "max32620",         None                    ),
    "0408": BoardInfo(  "MAX32625NEXPAQ",       "max32625",         None                    ),
    "0409": BoardInfo(  "MAX32630FTHR",         "max32630",         "max32630fthr.bin",     ),
    "0415": BoardInfo(  "MAX32625MBED",         "max32625",         "max32625mbed.bin",     ),
    "0416": BoardInfo(  "MAX32625PICO",         "max32625",         "max32625pico.bin",     ),
    "0417": BoardInfo(  "MAX32630MBED",         "max32630",         None                    ),
    "0418": BoardInfo(  "MAX32620FTHR",         "max32620",         "max32620fthr.bin",     ),
    "0420": BoardInfo(  "MAX32630HSP3",         "max32630",         None                    ),
    "0451": BoardInfo(  "MTB MXChip EMW3166",   "stm32f412xg",      "mtb_mxchip_emw3166.bin",),
    "0459": BoardInfo(  "MTB Advantech WISE-1530", "stm32f412xg",   "mtb_wise-1530.bin",    ),
    "0462": BoardInfo(  "MTB USI WM-BN-BM-22",  "stm32f412xg",      "mtb_usi_wm-bn-bm-22.bin",),
    "0602": BoardInfo(  "EV_COG_AD3029LZ",      "aducm3029",        None                    ),
    "0603": BoardInfo(  "EV_COG_AD4050LZ",      "aducm4050",        None                    ),
    "0700": BoardInfo(  "NUCLEO-F103RB",        "stm32f103rb",      None,                   ),
    "0705": BoardInfo(  "NUCLEO-F302R8",        "stm32f302r8",      None,                   ),
    "0710": BoardInfo(  "NUCLEO-L152RE",        "stm32l152re",      None,                   ),
    "0715": BoardInfo(  "NUCLEO-L053R8",        "stm32l053r8",      None,                   ),
    "0720": BoardInfo(  "NUCLEO-F401RE",        "stm32f401re",      None,                   ),
    "0725": BoardInfo(  "NUCLEO-F030R8",        "stm32f030r8",      None,                   ),
    "0730": BoardInfo(  "NUCLEO-F072RB",        "stm32f072rb",      None,                   ),
    "0735": BoardInfo(  "NUCLEO-F334R8",        "stm32f334r8",      None,                   ),
    "0740": BoardInfo(  "NUCLEO-F411RE",        "stm32f411re",      None,                   ),
    "0742": BoardInfo(  "NUCLEO-F413ZH",        "stm32f413zh",      None,                   ),
    "0743": BoardInfo(  "DISCO-F413ZH",         "stm32f413zh",      None,                   ),
    "0744": BoardInfo(  "NUCLEO-F410RB",        "stm32f410rb",      None,                   ),
    "0745": BoardInfo(  "NUCLEO-F303RE",        "stm32f303re",      None,                   ),
    "0746": BoardInfo(  "DISCO-F303VC",         "stm32f303vc",      None,                   ),
    "0747": BoardInfo(  "NUCLEO-F303ZE",        "stm32f303ze",      None,                   ),
    "0750": BoardInfo(  "NUCLEO-F091RC",        "stm32f091rc",      None,                   ),
    "0755": BoardInfo(  "NUCLEO-F070RB",        "stm32f070rb",      None,                   ),
    "0760": BoardInfo(  "NUCLEO-L073RZ",        "stm32l073rz",      None,                   ),
    "0764": BoardInfo(  "DISCO-L475VG-IOT01A",  "stm32l475xg",      "stm32l475vg_iot01a.bin",),
    "0765": BoardInfo(  "NUCLEO-L476RG",        "stm32l476rg",      None,                   ),
    "0770": BoardInfo(  "NUCLEO-L432KC",        "stm32l432kc",      None,                   ),
    "0774": BoardInfo(  "DISCO-L4R9I",          "stm32ler9i",       None,                   ),
    "0775": BoardInfo(  "NUCLEO-F303K8",        "stm32f303k8",      None,                   ),
    "0776": BoardInfo(  "NUCLEO-L4R5ZI",        "stm32l4r5zi",      None,                   ),
    "0777": BoardInfo(  "NUCLEO-F446RE",        "stm32f446re",      None,                   ),
    "0778": BoardInfo(  "NUCLEO-F446ZE",        "stm32f446ze",      None,                   ),
    "0779": BoardInfo(  "NUCLEO-L433RC-P",      "stm32l433rc",      None,                   ),
    "0780": BoardInfo(  "NUCLEO-L011K4",        "stm32l011k4",      None,                   ),
    "0781": BoardInfo(  "NUCLEO-L4R5ZI-P",      "stm32l4r5zi",      None,                   ),
    "0785": BoardInfo(  "NUCLEO-F042K6",        "stm32f042k6",      None,                   ),
    "0788": BoardInfo(  "DISCO-F469NI",         "stm32f469ni",      None,                   ),
    "0790": BoardInfo(  "NUCLEO-L031K6",        "stm32l031k6",      None,                   ),
    "0791": BoardInfo(  "NUCLEO-F031K6",        "stm32f031k6",      None,                   ),
    "0795": BoardInfo(  "DISCO-F429ZI",         "stm32f429zi",      None,                   ),
    "0796": BoardInfo(  "NUCLEO-F429ZI",        "stm32f429xi",      "nucleo_f429zi.bin",    ),
    "0797": BoardInfo(  "NUCLEO-F439ZI",        "stm32f439zi",      None,                   ),
    "0799": BoardInfo(  "NUCLEO-L073RZ",        "stm32l073rz",      None,                   ),
    "0805": BoardInfo(  "DISCO-L053C8",         "stm32l053c8",      None,                   ),
    "0810": BoardInfo(  "DISCO-F334C8",         "stm32f334c8",      None,                   ),
    "0812": BoardInfo(  "NUCLEO-F722ZE",        "stm32f722ze",      None,                   ),
    "0813": BoardInfo(  "NUCLEO-H743ZI",        "stm32h743zitx",    None,                   ),
    "0814": BoardInfo(  "DISCO-H747I",          "stm32h747xihx",    None,                   ),
    "0815": BoardInfo(  "DISCO-F746NG",         "stm32f746ng",      None,                   ),
    "0816": BoardInfo(  "NUCLEO-F746ZG",        "stm32f746zg",      None,                   ),
    "0817": BoardInfo(  "DISCO-F769NI",         "stm32f769ni",      None,                   ),
    "0818": BoardInfo(  "NUCLEO-F767ZI",        "stm32f767zi",      None,                   ),
    "0820": BoardInfo(  "DISCO-L476VG",         "stm32l476vg",      None,                   ),
    "0821": BoardInfo(  "NUCLEO-L452RE",        "stm32l452re",      None,                   ),
    "0822": BoardInfo(  "DISCO-L496AG",         "stm32l496ag",      None,                   ),
    "0823": BoardInfo(  "NUCLEO-L496ZG",        "stm32l496zg",      None,                   ),
    "0824": BoardInfo(  "LPCXpresso824-MAX",    "lpc824",           "l1_lpc824.bin",        ),
    "0826": BoardInfo(  "NUCLEO-F412ZG",        "stm32f412xg",      "nucleo_f412zg.bin",    ),
    "0827": BoardInfo(  "NUCLEO-L486RG",        "stm32l486rg",      None,                   ),
    "0828": BoardInfo(  "NUCLEO-L496ZG-P",      "stm32l496zg",      None,                   ),
    "0829": BoardInfo(  "NUCLEO-L452RE-P",      "stm32l452re",      None,                   ),
    "0830": BoardInfo(  "DISCO-F407VG",         "stm32f407vg",      None,                   ),
    "0833": BoardInfo(  "DISCO-L072CZ-LRWAN1",  "stm32l072cz",      None,                   ),
    "0835": BoardInfo(  "NUCLEO-F207ZG",        "stm32f207zg",      None,                   ),
    "0836": BoardInfo(  "NUCLEO-H743ZI2",       "stm32h743zitx",    None,                   ),
    "0839": BoardInfo(  "NUCLEO-WB55RG",        "stm32wb55rgvx",    None,                   ),
    "0840": BoardInfo(  "B96B-F446VE",          "stm32f446ve",      None,                   ),
    "0854": BoardInfo(  "NUCLEO-L552ZE-Q",      "stm32l552ze",      None,                   ),
    "0855": BoardInfo(  "DISCO-L562QE",         "stm32l562qe",      None,                   ),
    "0879": BoardInfo(  "NUCLEO-F756ZG",        "stm32f756zg",      None,                   ),
    "1010": BoardInfo(  "mbed NXP LPC1768",     "lpc1768",          "l1_lpc1768.bin",       ),
    "1017": BoardInfo(  "mbed HRM1017",         "nrf51",            "l1_nrf51.bin",         ),
    "1018": BoardInfo(  "Switch-Science-mbed-LPC824", "lpc824",     "l1_lpc824.bin",        ),
    "1019": BoardInfo(  "mbed TY51822r3",       "nrf51",            "l1_nrf51.bin",         ),
    "1040": BoardInfo(  "mbed NXP LPC11U24",    "lpc11u24",         "l1_lpc11u24.bin",      ),
    "1050": BoardInfo(  "NXP LPC800-MAX",       "lpc800",           "l1_lpc800.bin",        ),
    "1054": BoardInfo(  "LPCXpresso54114-MAX",  "lpc54114",         "l1_lpc54114.bin",      ),
    "1056": BoardInfo(  "LPCXpresso54608-MAX",  "lpc54608",         "l1_lpc54608.bin",      ),
    "1060": BoardInfo(  "EA-LPC4088",           "lpc4088qsb",       "l1_lpc4088qsb.bin",    ),
    "1068": BoardInfo(  "LPC11U68",             "lpc11u68jbd100",   None,                   ),
    "1062": BoardInfo(  "EA-LPC4088-Display-Module", "lpc4088dm",   "l1_lpc4088dm.bin",     ),
    "1070": BoardInfo(  "nRF51822-mKIT",        "nrf51",            "l1_nrf51.bin",         ),
    "1080": BoardInfo(  "mBuino",               "lpc11u24",         "l1_lpc11u24.bin",      ),
    "1090": BoardInfo(  "RedBearLab-nRF51822",  "nrf51",            "l1_nrf51.bin",         ),
    "1093": BoardInfo(  "RedBearLab-BLE-Nano2", "nrf52",            "l1_nrf52-dk.bin",      ),
    "1095": BoardInfo(  "RedBearLab-BLE-Nano",  "nrf51",            "l1_nrf51.bin",         ),
    "1100": BoardInfo(  "nRF51-DK",             "nrf51",            "l1_nrf51-dk.bin",      ),
    "1101": BoardInfo(  "nRF52-DK",             "nrf52",            "l1_nrf52-dk.bin",      ),
    "1102": BoardInfo(  "nRF52840-DK",          "nrf52840",         "l1_nrf52840-dk.bin",   ),
    "1114": BoardInfo(  "mbed LPC1114FN28",     "lpc11xx_32",       "l1_mbed_LPC1114FN28.bin",),
    "1120": BoardInfo(  "nRF51-Dongle",         "nrf51",            "l1_nrf51.bin",         ),
    "1200": BoardInfo(  "NCS36510-EVK",         "ncs36510",         "l1_ncs36510-evk.bin",  ),
    "1234": BoardInfo(  "u-blox-C027",          "lpc1768",          "l1_lpc1768.bin",       ),
    "1236": BoardInfo(  "u-blox EVK-ODIN-W2",   "stm32f439xi",      "ublox_evk_odin_w2.bin",),
    "1237": BoardInfo(  "u-blox-EVK-NINA-B1",   "nrf52",            "l1_nrf52-dk.bin",      ),
    "12A0": BoardInfo(  "Calliope-mini",        "nrf51",            None,                   ),
    "1549": BoardInfo(  "LPC1549",              "lpc1549jbd100",    None,                   ),
    "1600": BoardInfo(  "Bambino 210",          "lpc4330",          "l1_lpc4330.bin",       ),
    "1605": BoardInfo(  "Bambino 210E",         "lpc4330",          "l1_lpc4330.bin",       ),
    "1900": BoardInfo(  "CY8CKIT-062-WIFI-BT",  "cy8c6xx7",         "l1_cy8c6xx7.bin",      ),
    "1901": BoardInfo(  "CY8CPROTO-062-4343W",  "cy8c6xxA",         "l1_cy8c6xxa.bin",      ),
    "1902": BoardInfo(  "CY8CKIT-062-BLE",      "cy8c6xx7",         "l1_cy8c6xx7.bin",      ),
    "1903": BoardInfo(  "CYW9P62S1-43012EVB-01","cy8c6xx7",         "l1_cy8c6xx7.bin",      ),
    "1904": BoardInfo(  "CY8CPROTO-063-BLE",    "cy8c6xx7",         "l1_cy8c6xx7.bin",      ),
    "1905": BoardInfo(  "CY8CKIT-062-4343W",    "cy8c6xxA",         "l1_cy8c6xxa.bin",      ),
    "1906": BoardInfo(  "CYW943012P6EVB-01",    "cy8c6xx7",         "l1_cy8c6xx7.bin",      ),
    "1907": BoardInfo(  "CY8CPROTO-064-SB",     "cy8c64xx_cm4",     "l1_cy8c6xx7.bin",      ),
    "1908": BoardInfo(  "CYW9P62S1-43438EVB-01","cy8c6xx7",         "l1_cy8c6xx7.bin",      ),
    "1909": BoardInfo(  "CY8CPROTO-062S2-43012","cy8c6xxA",         "l1_cy8c6xxa.bin",      ),
    "190A": BoardInfo(  "CY8CKIT-064S2-4343W",  "cy8c64xA_cm4",     "l1_cy8c6xxa.bin",      ),
    "190B": BoardInfo(  "CY8CKIT-062S2-43012",  "cy8c6xxA",         "l1_062S2-43012.bin",   ),
    "190D": BoardInfo(  "AUGUST_CYW43012",      "cy8c64xx_cm4",     "l1_cy8c6xx7.bin",      ),
    "190E": BoardInfo(  "CY8CPROTO-062S3-4343W","cy8c6xx5",         "l1_cy8c6xxa.bin",      ),
    "2201": BoardInfo(  "WIZwik_W7500",         "w7500",            "l1_w7500mbed.bin",     ),
    "2600": BoardInfo(  "ep_agora",             "nrf52840",         None,                   ),
    "3300": BoardInfo(  "CC3220SF_LaunchXL",    "cc3220sf",         "l1_cc3220sf.bin",      ),
    "4337": BoardInfo(  "LPC4337",              "lpc4337",          None,                   ),
    "4600": BoardInfo(  "Realtek RTL8195AM",    "rtl8195am",        "l1_rtl8195am.bin",     ),
    "5006": BoardInfo(  "Arm Musca-A1",         "musca_a1",         "l1_musca_a1.bin",      ),
    "5007": BoardInfo(  "Arm Musca-B1",         "musca_b1",         "l1_musca_b1.bin",      ),
    "7402": BoardInfo(  "mbed 6LoWPAN Border Router HAT", "k64f",   "l1_k64f.bin",          ),
    "7778": BoardInfo(  "Teensy 3.1",           "mk20dx256vlh7",    None,                   ),
    "8080": BoardInfo(  "L-Tek FF1705",         "stm32l151cc",      None,                   ),
    "8081": BoardInfo(  "L-Tek FF-LPC546XX",    "lpc54606",         None,                   ),
    "9004": BoardInfo(  "Arch Pro",             "lpc1768",          "l1_lpc1768.bin",       ),
    "9009": BoardInfo(  "Arch BLE",             "nrf51",            "l1_nrf51.bin",         ),
    "9012": BoardInfo(  "Seeed Tiny BLE",       "nrf51",            "l1_nrf51.bin",         ),
    "9014": BoardInfo(  "Seeed 96Boards Nitrogen", "nrf52",         "l1_nrf52-dk.bin",      ),
    "9900": BoardInfo(  "micro:bit",            "nrf51",            "l1_microbit.bin",      ),
    "9901": BoardInfo(  "micro:bit",            "nrf51",            "l1_microbit.bin",      ),
    "C004": BoardInfo(  "tinyK20",              "k20d50m",          "l1_k20d50m.bin",       ),
    "C006": BoardInfo(  "VBLUno51",             "nrf51",            "l1_nrf51.bin",         ),
}
