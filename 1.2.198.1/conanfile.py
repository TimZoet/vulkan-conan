from conans import ConanFile
import os

class VulkanConan(ConanFile):
    name = "vulkan"
    version = "1.2.198.1"
    description = "..."
    settings = ("os", "compiler", "build_type", "arch")

    def export_sources(self):
        self.copy("Lib/shaderc_combined.lib")
        self.copy("Lib/shaderc_combinedd.lib")
        self.copy("Lib/vulkan-1.lib")
        self.copy("Include/vulkan/*")
        self.copy("Include/shaderc/*")

    def package_info(self):
        self.cpp_info.components["core"].libs = ["vulkan-1"]
        if self.settings.build_type == "Debug":
            self.cpp_info.components["shaderc"].libs = ["shaderc_combinedd"]
        else:
            self.cpp_info.components["shaderc"].libs = ["shaderc_combined"]

    def package(self):
        self.copy("*", dst="lib", src="Lib")
        self.copy("*", dst="include/vulkan", src="Include/vulkan")
        self.copy("*", dst="include/shaderc", src="Include/shaderc")
