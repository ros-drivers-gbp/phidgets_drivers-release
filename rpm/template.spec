Name:           ros-indigo-phidgets-api
Version:        0.2.3
Release:        1%{?dist}
Summary:        ROS phidgets_api package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/phidgets_api
Source0:        %{name}-%{version}.tar.gz

Requires:       libusbx
Requires:       ros-indigo-libphidgets
BuildRequires:  libusbx-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-libphidgets

%description
A C++ Wrapper for the Phidgets C API

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Feb 17 2017 Martin Guenther <martin.guenther@dfki.de> - 0.2.3-1
- Autogenerated by Bloom

* Fri Feb 17 2017 Martin Guenther <martin.guenther@dfki.de> - 0.2.3-0
- Autogenerated by Bloom

* Mon Mar 23 2015 Murilo FM <muhrix@gmail.com> - 0.2.2-0
- Autogenerated by Bloom

* Thu Jan 15 2015 Murilo FM <muhrix@gmail.com> - 0.2.1-0
- Autogenerated by Bloom

