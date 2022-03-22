import sys
import os
import yaml

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from util import getDataframe as gd

getData = gd.GetData()
# Instance variables 테스트
# print(f"{gd.GetData.file_list}")
print(f"Instance variables: {getData.file_list}")
print(f"Class variables: {gd.GetData.test_list}")

with open('./data/platform.yml') as f:
    platform = yaml.safe_load(f)

#print(platform)
tmp = "SSG.COM"

print(platform)

if tmp in platform['platform']:
    print('in tmp')