# Types of Modules internal external
import math
print(math.sqrt(16))

# importing own module

import my_module

my_module.cube(22)

import requests

# h_code = requests.get("https://play.google.com/googleplaygames?utm_source=apac_med&utm_medium=hasem&utm_content=Jan0325&utm_campaign=Evergreen&pcampaignid=MKT-EDR-apac-in-1710488-med-hasem-py-Evergreen-Jan0325-Text_Search_BKWS-BKWS-BASDMF%7CONSEM_kwid_43700078556916250_creativeid_676139709508_device_c&gad_source=1&gad_campaignid=20622030410&gbraid=0AAAAApZHpVvMlQy-FEyQ50GkQzrMnUaWs&gclid=Cj0KCQjwmK_CBhCEARIsAMKwcD4hm8DGU6NbrHNXf-Pq_iesQVZH_LaNYem-6S01AIfC3ipM3L5JQuoaAhk8EALw_wcB&gclsrc=aw.ds")
# print(h_code.text)