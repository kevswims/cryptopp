from conans import ConanFile, tools


class CryptoppConan(ConanFile):
    name = "cryptopp"
    version = "5.6.5"
    url = "www.cryptopp.com"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "*"

    def build(self):
        cmd = tools.msvc_build_command(self.settings, "cryptest.sln")
        self.run(cmd)

    def package(self):
        self.copy("*.h", dst="include", keep_path=False)
        self.copy("*.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["cryptlib"]
