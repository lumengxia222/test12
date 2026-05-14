#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
域名HTTP/HTTPS访问性检测脚本
功能：
1. 读取CSV文件中的域名列表
2. 检测每个域名的HTTP和HTTPS是否能访问
3. 在表格中标注可访问的协议（HTTP/HTTPS/Both）
"""

import csv
import os
import sys
import requests
import urllib3
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

# 屏蔽SSL证书验证警告
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def check_domain_access(domain, timeout=5):
    """