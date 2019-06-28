Name:           ros-melodic-phidgets-imu
Version:        0.7.9
Release:        1%{?dist}
Summary:        ROS phidgets_imu package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/phidgets_imu
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-melodic-diagnostic-aggregator
Requires:       ros-melodic-diagnostic-msgs
Requires:       ros-melodic-diagnostic-updater
Requires:       ros-melodic-imu-filter-madgwick
Requires:       ros-melodic-nodelet
Requires:       ros-melodic-phidgets-api
Requires:       ros-melodic-pluginlib
Requires:       ros-melodic-roscpp
Requires:       ros-melodic-sensor-msgs
Requires:       ros-melodic-std-msgs
Requires:       ros-melodic-std-srvs
Requires:       ros-melodic-tf
BuildRequires:  ros-melodic-catkin
BuildRequires:  ros-melodic-diagnostic-msgs
BuildRequires:  ros-melodic-diagnostic-updater
BuildRequires:  ros-melodic-nodelet
BuildRequires:  ros-melodic-phidgets-api
BuildRequires:  ros-melodic-pluginlib
BuildRequires:  ros-melodic-roscpp
BuildRequires:  ros-melodic-roslaunch
BuildRequires:  ros-melodic-sensor-msgs
BuildRequires:  ros-melodic-std-msgs
BuildRequires:  ros-melodic-std-srvs
BuildRequires:  ros-melodic-tf

%description
Driver for the Phidgets Spatial 3/3/3 devices

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/melodic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/melodic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/melodic/setup.sh" ]; then . "/opt/ros/melodic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/melodic

%changelog
* Fri Jun 28 2019 Martin Guenther <martin.guenther@dfki.de> - 0.7.9-1
- Autogenerated by Bloom

* Mon May 06 2019 Martin Guenther <martin.guenther@dfki.de> - 0.7.8-1
- Autogenerated by Bloom

* Wed Sep 19 2018 Martin Guenther <martin.guenther@dfki.de> - 0.7.7-0
- Autogenerated by Bloom

* Thu Aug 09 2018 Martin Guenther <martin.guenther@dfki.de> - 0.7.6-0
- Autogenerated by Bloom

