Name:           ros-indigo-pid
Version:        0.0.9
Release:        0%{?dist}
Summary:        ROS pid package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/pid
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-dynamic-reconfigure
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-std-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-dynamic-reconfigure
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs

%description
Launch a PID control node.

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
* Sun Dec 27 2015 Andy Zelenak <andyz@utexas.edu> - 0.0.9-0
- Autogenerated by Bloom

* Sun Jul 26 2015 Andy Zelenak <andyz@utexas.edu> - 0.0.7-0
- Autogenerated by Bloom

* Tue Jun 09 2015 Andy Zelenak <andyz@utexas.edu> - 0.0.6-0
- Autogenerated by Bloom

* Tue Jun 09 2015 Andy Zelenak <andyz@utexas.edu> - 0.0.5-0
- Autogenerated by Bloom

* Sat Mar 14 2015 Andy Zelenak <andyz@utexas.edu> - 0.0.3-0
- Autogenerated by Bloom

* Fri Mar 13 2015 Andy Zelenak <andyz@utexas.edu> - 0.0.2-0
- Autogenerated by Bloom

* Sun Mar 08 2015 Andy Zelenak <andyz@utexas.edu> - 0.0.1-0
- Autogenerated by Bloom

