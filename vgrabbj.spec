Summary:	A command-line v4l grabber
Name:		vgrabbj
Version:	0.9.6
Release:	9
License:	GPLv2+
Group:		Video
Url:		https://vgrabbj.gecius.de/
Source0:	http://vgrabbj.gecius.de/vgrabbj/%{name}-%{version}.tar.bz2
Patch0:		vgrabbj-0.9.6-gcc4.patch
Patch1:		vgrabbj-0.9.6-fix-str-fmt.patch
Patch2:		vgrabbj-0.9.6-libv4l1.patch
Patch3:		vgrabbj-0.9.6-off-by-one.patch
Patch4:		vgrabbj-0.9.6-automake-1.13.patch
BuildRequires:	jpeg-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(libv4l1)
BuildRequires:	pkgconfig(zlib)

%description
Vgrabbj is a commandline tool that grabs an image from a 24-bit v4l device
(like a webcam) and save it as a ppm, png or jpg file. It can imprint a label
(with time or not) onto the image. It can also be used in stopmotion program
to acquire images.

%files
%doc AUTHORS ChangeLog README THANKS TODO
%{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.conf.5*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p0
%patch2 -p1
%patch3 -p1
%patch4 -p1 -b .automake-1_13

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

