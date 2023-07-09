# TODO: review configure options:
# - FTL_JIT on !x86_64?
# - WEB_RTC+MEDIA_STREAM (experimental; BR: openwebrtc)
# - AVIF? (experimental; BR: libavif-devel >= 0.9.0)
# - JPEGXL? (experimental; BR: libjxl-devel)
# - THUNDER? (BR: Thunder + ThunderClientLibraries)
#
# Conditional build:
%bcond_without	introspection	# GObject introspection
%bcond_without	wayland		# Wayland target (requires GTK+ wayland target)
%bcond_with	lowmem		# try to reduce build memory usage by adjusting gcc gc
%bcond_with	lowmem2		# try to reduce build memory usage by disabling unified build (long)
#
# it's not possible to build this with debuginfo on 32bit archs due to
# memory constraints during linking
%ifarch %{ix86} x32
%define		_enable_debug_packages		0
%endif
Summary:	Port of WebKit embeddable web component to GTK 4
Summary(pl.UTF-8):	Port osadzalnego komponentu WWW WebKit do GTK 4
Name:		gtk-webkit5
# 2.38.x is the last with gtk-webkit5 library
Version:	2.38.6
Release:	5
License:	BSD-like
Group:		X11/Libraries
Source0:	https://webkitgtk.org/releases/webkitgtk-%{version}.tar.xz
# Source0-md5:	a50290fdc80842b1ae8be1e1147b5679
Patch0:		%{name}-x32.patch
Patch1:		%{name}-icu59.patch
Patch2:		%{name}-parallel-gir.patch
Patch3:		%{name}-driver-version-suffix.patch
Patch4:		%{name}-gcc13.patch
URL:		https://webkitgtk.org/
BuildRequires:	/usr/bin/ld.gold
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGLESv2-devel
BuildRequires:	at-spi2-core-devel >= 2.5.3
BuildRequires:	atk-devel >= 1:2.16.0
BuildRequires:	bubblewrap >= 0.3.1
BuildRequires:	cairo-devel >= 1.16.0
BuildRequires:	cmake >= 3.20
BuildRequires:	docbook-dtd412-xml
BuildRequires:	enchant2-devel >= 2
BuildRequires:	fontconfig-devel >= 2.13.0
BuildRequires:	freetype-devel >= 1:2.9.0
BuildRequires:	gcc-c++ >= 6:7.3.0
BuildRequires:	gettext-devel
BuildRequires:	gettext-tools
BuildRequires:	gi-docgen
BuildRequires:	glib2-devel >= 1:2.67.1
BuildRequires:	glibc-misc
%{?with_introspection:BuildRequires:	gobject-introspection-devel >= 1.32.0}
BuildRequires:	gperf >= 3.0.1
BuildRequires:	gstreamer-devel >= 1.14
BuildRequires:	gstreamer-gl-devel >= 1.10.0
# codecparsers,mpegts with -DUSE_GSTREAMER_MPEGTS=ON
#BuildRequires:	gstreamer-plugins-bad-devel >= 1.10.0
# app,audio,fft,pbutils,tag,video
BuildRequires:	gstreamer-plugins-base-devel >= 1.10.0
BuildRequires:	gtk4-devel >= 4.0
BuildRequires:	gtk-doc >= 1.10
BuildRequires:	harfbuzz-devel >= 1.4.2
BuildRequires:	harfbuzz-icu-devel >= 1.4.2
BuildRequires:	hyphen-devel
BuildRequires:	lcms2-devel >= 2
BuildRequires:	libgcrypt-devel >= 1.7.0
BuildRequires:	libicu-devel >= 61.2
BuildRequires:	libjpeg-devel
BuildRequires:	libmanette-devel >= 0.2.4
BuildRequires:	libnotify-devel
BuildRequires:	libpng-devel
BuildRequires:	libseccomp-devel
BuildRequires:	libsecret-devel
BuildRequires:	libsoup3-devel >= 3.0
# -std=c++2a
BuildRequires:	libstdc++-devel >= 6:8.3
BuildRequires:	libtasn1-devel
BuildRequires:	libwebp-devel
BuildRequires:	libwpe-devel >= 1.3.0
BuildRequires:	libxml2-devel >= 1:2.8.0
BuildRequires:	libxslt-devel >= 1.1.7
BuildRequires:	openjpeg2-devel >= 2.2.0
BuildRequires:	pango-devel >= 1:1.32.0
BuildRequires:	perl-base >= 1:5.10.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.7.0
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.699
BuildRequires:	ruby >= 1:1.9
BuildRequires:	ruby-modules >= 1:1.9
BuildRequires:	sqlite3-devel >= 3
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
%if %{with wayland}
BuildRequires:	wayland-devel
BuildRequires:	wayland-egl-devel
BuildRequires:	wayland-protocols >= 1.12
%endif
BuildRequires:	wpebackend-fdo-devel >= 1.6.0
BuildRequires:	woff2-devel >= 1.0.2
BuildRequires:	xdg-dbus-proxy
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libXcomposite-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	at-spi2-core-libs >= 2.5.3
Requires:	atk >= 1:2.16.0
Requires:	cairo >= 1.16.0
Requires:	fontconfig-libs >= 2.13.0
Requires:	freetype >= 1:2.9.0
Requires:	glib2 >= 1:2.67.1
Requires:	gstreamer >= 1.2.3
Requires:	gstreamer-plugins-base >= 1.2.3
Requires:	gtk4 >= 4.0
Requires:	harfbuzz >= 1.4.2
Requires:	libgcrypt >= 1.7.0
Requires:	libsoup3 >= 3.0
Requires:	libwpe >= 1.3.0
Requires:	libxml2 >= 1:2.8.0
Requires:	libxslt >= 1.1.7
Requires:	openjpeg2 >= 2.2.0
Requires:	pango >= 1:1.32.0
Requires:	woff2 >= 1.0.2
Requires:	wpebackend-fdo >= 1.6.0
%{?with_introspection:Conflicts:	gir-repository < 0.6.5-7}
# Source/JavaScriptCore/CMakeLists.txt /WTF_CPU_
ExclusiveArch:	%{ix86} %{x8664} x32 %{arm} aarch64 hppa mips ppc ppc64 ppc64le s390 s390x sh4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# __once_call, __once_called non-function symbols from libstdc++
%define		skip_post_check_so	lib.*gtk-4.0.*

%description
gtk-webkit5 is a port of the WebKit embeddable web component to GTK 4.

%description -l pl.UTF-8
gtk-webkit5 to port osadzalnego komponentu WWW WebKit do GTK+ 4.

%package devel
Summary:	Development files for WebKit for GTK 4
Summary(pl.UTF-8):	Pliki programistyczne komponentu WebKit dla GTK 4
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.67.1
Requires:	gtk4-devel >= 4.0
Requires:	libsoup3-devel >= 3.0
Requires:	libstdc++-devel >= 6:8.3

%description devel
Development files for WebKit for GTK 4.

%description devel -l pl.UTF-8
Pliki programistyczne komponentu WebKit dla GTK 4.

%package apidocs
Summary:	API documentation for WebKit GTK 4 port
Summary(pl.UTF-8):	Dokumentacja API portu WebKitu do GTK 4
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
API documentation for WebKit GTK 4 port.

%description apidocs -l pl.UTF-8
Dokumentacja API portu WebKitu do GTK 4.

%prep
%setup -q -n webkitgtk-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%if %{with lowmem}
CXXFLAGS="%{rpmcxxflags} --param ggc-min-expand=20 --param ggc-min-heapsize=65536"
%endif
install -d build-gtk4
%cmake -B build-gtk4 \
	-DENABLE_GEOLOCATION=ON \
	-DENABLE_GTKDOC=ON \
	%{!?with_introspection:-DENABLE_INTROSPECTION=OFF} \
	%{?with_lowmem2:-DENABLE_UNIFIED_BUILDS=OFF} \
	-DENABLE_VIDEO=ON \
	%{!?with_wayland:-DENABLE_WAYLAND_TARGET=OFF} \
	-DENABLE_WEB_AUDIO=ON \
	-DENABLE_WEBGL=ON \
%ifarch x32
	-DENABLE_C_LOOP=ON \
	-DENABLE_JIT=OFF \
	-DENABLE_SAMPLING_PROFILER=OFF \
%endif
%ifarch %{ix86} %{x8664} x32
	-DHAVE_SSE2_EXTENSIONS=ON \
%endif
	-DPORT=GTK \
	-DSHOULD_INSTALL_JS_SHELL=ON \
	-DUSE_GTK4=ON

%{__make} -C build-gtk4

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build-gtk4 install \
	DESTDIR=$RPM_BUILD_ROOT

%if "%{_gtkdocdir}" != "%{_datadir}/gtk-doc/html"
install -d $RPM_BUILD_ROOT%{_gtkdocdir}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/gtk-doc/html/* $RPM_BUILD_ROOT%{_gtkdocdir}
%endif

%find_lang WebKit2GTK-5.0

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f WebKit2GTK-5.0.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/WebKitWebDriver-5.0
%attr(755,root,root) %{_libdir}/libwebkit2gtk-5.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libwebkit2gtk-5.0.so.0
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-5.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjavascriptcoregtk-5.0.so.0
%if %{with introspection}
%{_libdir}/girepository-1.0/JavaScriptCore-5.0.typelib
%{_libdir}/girepository-1.0/WebKit2-5.0.typelib
%{_libdir}/girepository-1.0/WebKit2WebExtension-5.0.typelib
%endif
%if "%{_libexecdir}" != "%{_libdir}"
%dir %{_libexecdir}/webkit2gtk-5.0
%endif
%attr(755,root,root) %{_libexecdir}/webkit2gtk-5.0/MiniBrowser
%attr(755,root,root) %{_libexecdir}/webkit2gtk-5.0/WebKitNetworkProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-5.0/WebKitWebProcess
%attr(755,root,root) %{_libexecdir}/webkit2gtk-5.0/jsc
%dir %{_libdir}/webkit2gtk-5.0
%dir %{_libdir}/webkit2gtk-5.0/injected-bundle
%attr(755,root,root) %{_libdir}/webkit2gtk-5.0/injected-bundle/libwebkit2gtkinjectedbundle.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libwebkit2gtk-5.0.so
%attr(755,root,root) %{_libdir}/libjavascriptcoregtk-5.0.so
%if %{with introspection}
%{_datadir}/gir-1.0/JavaScriptCore-5.0.gir
%{_datadir}/gir-1.0/WebKit2-5.0.gir
%{_datadir}/gir-1.0/WebKit2WebExtension-5.0.gir
%endif
%{_includedir}/webkitgtk-5.0
%{_pkgconfigdir}/javascriptcoregtk-5.0.pc
%{_pkgconfigdir}/webkit2gtk-5.0.pc
%{_pkgconfigdir}/webkit2gtk-web-extension-5.0.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/javascriptcoregtk-5.0
%{_gtkdocdir}/webkit2gtk-5.0
%{_gtkdocdir}/webkit2gtk-web-extension-5.0
