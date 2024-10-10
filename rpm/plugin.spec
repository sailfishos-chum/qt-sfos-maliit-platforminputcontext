Summary: Qt Platform Input Contexts for Maliit keyboard
Name: qt6-sfos-maliit-platforminputcontext
Version: 1.0.0
Release: 1%{?dist}

License: LGPLv2
Url:     https://github.com/sailfishos-open/maliit-framework
Source0: %{name}-%{version}.tar.bz2

%global __provides_exclude_from ^%{_qt6_plugindir}/platforminputcontexts/.*\\.so$

BuildRequires: make
BuildRequires: cmake

BuildRequires: qt6-qtbase-devel
BuildRequires: qt6-qtbase-private-devel
BuildRequires: qt6-qtdeclarative-devel
%{?_qt6:Requires: %{_qt6}%{?_isa} = %{_qt6_version}}

%description
This input plugin links Maliit keyboard provided by Sailfish OS to
applications using newer Qt.

%prep
%autosetup -n %{name}-%{version}/upstream


%build

%cmake_qt6 \
    -Denable-docs=OFF \
    -Denable-tests=OFF \
    -Denable-glib=OFF \
    -Denable-xcb=OFF \
    -Denable-wayland=OFF \
    -Denable-wayland-gtk=OFF \
    -Denable-qt6-inputcontext=ON \
    -Denable-hwkeyboard=OFF

%cmake_build

%install

%cmake_install

%files
%{_qt6_plugindir}/platforminputcontexts/libmaliitplatforminputcontextplugin.so
