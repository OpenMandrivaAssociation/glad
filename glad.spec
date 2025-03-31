%define major   0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary: GL/GLES/EGL/GLX/WGL Loader-Generator
Name:    glad
Version: 0.1.36
Release: 1
Group:   Development/Other
License: MIT
Url:     https://github.com/Dav1dde/glad
Source:  https://github.com/Dav1dde/glad/archive/refs/tags/v%{version}.tar.gz
Patch:   lib_install_path.patch

BuildRequires: cmake
BuildRequires: ninja
BuildRequires: python

%description
GL/GLES/EGL/GLX/WGL Loader-Generator based on the official specs.

%package -n %{libname}
Summary: Package for %{name}
Group:   System/Libraries

%description -n %{libname}
Shared library for %{name}.

%package -n %{devname}
Summary:  Development package for %{name}
Group:    Development/Libraries
Requires: %{libname} = %{version}-%{release}
Provides: %{name} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{devname}
Header files for development with %{name}.

%prep
%autosetup

%build
%cmake -G Ninja \
       -DCMAKE_BUILD_TYPE=Release \
       -DGLAD_ALL_EXTENSIONS=ON \
       -DGLAD_REPRODUCIBLE=ON \
       -DGLAD_INSTALL=ON
%ninja_build

%install
%ninja_install -C build

%files -n %{libname}
%{_libdir}/lib%{name}.so

%files -n %{devname}
%license LICENSE
%doc example/c example/c++
%{_includedir}/KHR/khrplatform.h
%{_includedir}/%{name}/
%{_libdir}/cmake/%{name}/
