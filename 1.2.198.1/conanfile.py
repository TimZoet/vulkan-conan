from conan import ConanFile
from conan.tools.files import copy

class VulkanConan(ConanFile):
    name = "vulkan"
    version = "1.2.198.1"
    description = "..."
    settings = ("os", "compiler", "build_type", "arch")

    def export_sources(self):
        copy(self, "Lib/shaderc_combined.lib", self.recipe_folder, self.export_sources_folder)
        copy(self, "Lib/shaderc_combinedd.lib", self.recipe_folder, self.export_sources_folder)
        copy(self, "Lib/vulkan-1.lib", self.recipe_folder, self.export_sources_folder)
        copy(self, "Include/vulkan/*", self.recipe_folder, self.export_sources_folder)
        copy(self, "Include/shaderc/*", self.recipe_folder, self.export_sources_folder)

    def package_info(self):
        self.cpp_info.components["core"].libs = ["vulkan-1"]
        if self.settings.build_type == "Debug":
            self.cpp_info.components["shaderc"].libs = ["shaderc_combinedd"]
        else:
            self.cpp_info.components["shaderc"].libs = ["shaderc_combined"]

    def package(self):
        copy(self, "Lib/*", self.export_sources_folder, self.package_folder)
        copy(self, "Include/vulkan/*", self.export_sources_folder, self.package_folder)
        copy(self, "Include/shaderc/*", self.export_sources_folder, self.package_folder)
