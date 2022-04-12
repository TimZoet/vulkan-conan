# Vulkan conanfile.py

Conan scripts to properly integrate the Vulkan SDK into your Conan workflow. With these scripts, the SDK can be turned
into a Conan package.

To prevent problems with CMake's `find_package`, do the following:

* Remove any environment variables referring to the Vulkan SDK (e.g. `VK_SDK_PATH`, `VULKAN_SDK`).
* Remove the `FindVulkan.cmake` file in your CMake install.

To export the `vulkan` package to your local cache:

* Add the `conanfile.py` for the desired version to the root of the unpacked Vulkan SDK.
* From the root, run `conan export . user/channel`.

The `vulkan/version@user/channel` package is then available:

```py
class MyConan(ConanFile):
    def requirements(self):
        self.requires("vulkan/1.2.198.1@user/channel")
```

In one of your CMake scripts, you can now link to the libraries:

```cmake
find_package(vulkan REQUIRED)
add_executable(your-exe main.cpp)
target_link_libraries(your-exe PUBLIC vulkan::vulkan)
```
