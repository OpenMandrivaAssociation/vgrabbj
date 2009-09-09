%define name vgrabbj
%define version 0.9.6
%define release %mkrel 4

Name: %{name}
Summary: A command-line v4l grabber
Version: %{version}
Release: %{release}

Source: %{name}-%{version}.tar.bz2
Patch: %{name}-%{version}-gcc4.patch
URL: http://vgrabbj.gecius.de/
License: GPL
Group: Video
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: jpeg-devel
BuildRequires: zlib-devel
BuildRequires: tiff-devel
BuildRequires: freetype-devel
BuildRequires: png-devel

%description
Vgrabbj is a commandline tool that grabs an image from a 24-bit v4l device 
(like a webcam) and save it as a ppm, png or jpg file.
It can imprint a label (with time or not) onto the image.
It can also be used in stopmotion program to acquire images.

%prep
%setup -q
%patch -p1

%build
%configure
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README THANKS TODO

%{_bindir}/%name
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*

