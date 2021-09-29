%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-phidgets-drivers
Version:        1.0.3
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS phidgets_drivers package

License:        BSD, LGPL
URL:            http://ros.org/wiki/phidgets_drivers
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       ros-noetic-libphidget22
Requires:       ros-noetic-phidgets-accelerometer
Requires:       ros-noetic-phidgets-analog-inputs
Requires:       ros-noetic-phidgets-api
Requires:       ros-noetic-phidgets-digital-inputs
Requires:       ros-noetic-phidgets-digital-outputs
Requires:       ros-noetic-phidgets-gyroscope
Requires:       ros-noetic-phidgets-high-speed-encoder
Requires:       ros-noetic-phidgets-ik
Requires:       ros-noetic-phidgets-magnetometer
Requires:       ros-noetic-phidgets-motors
Requires:       ros-noetic-phidgets-msgs
Requires:       ros-noetic-phidgets-spatial
Requires:       ros-noetic-phidgets-temperature
BuildRequires:  ros-noetic-catkin
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
API and ROS drivers for Phidgets devices

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    -DCATKIN_BUILD_BINARY_PACKAGE="1" \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%files
/opt/ros/noetic

%changelog
* Wed Sep 29 2021 Martin Günther <martin.guenther@dfki.de> - 1.0.3-1
- Autogenerated by Bloom

* Tue Mar 09 2021 Martin Günther <martin.guenther@dfki.de> - 1.0.2-1
- Autogenerated by Bloom

* Thu Jun 04 2020 Martin Günther <martin.guenther@dfki.de> - 1.0.1-1
- Autogenerated by Bloom

* Wed Jun 03 2020 Martin Günther <martin.guenther@dfki.de> - 1.0.0-1
- Autogenerated by Bloom

