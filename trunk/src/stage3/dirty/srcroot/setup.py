from setuptools import setup, find_packages
setup(
    #套件名稱
    name = "uimeter",
    #作者名稱
    author = "Shang-Pin Chen (as Shan-Bin Chen, DreamerC)",
    #作者信箱
    auth_email = "dreamerwolf.tw+uimeter@gmail.com",
    #版權說明
    copyright = "Copyright 2009~ Sheng-Pin Chen and contributors"
    #授權
    license = "GPL Version 2 (http://www.gnu.org/licenses/old-licenses/gpl-2.0.html)",
    #首頁
    url = "http://uimeter.google.com/",
    #下載連結
    download_url = "http://code.google.com/p/uimeter",
    #版本
    version = "0.0.1",
    #關鍵字
    keywords = "interface, benchmark",
    packages = find_packages(),
    long_description = """
    Analyse user activity and decrease the time of learning processes.
    """,
    #需要的軟體版本
    install_requires = [],
    #需要一起打包的檔案
    package_data = {
    }
)

