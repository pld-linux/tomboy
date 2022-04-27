Summary:	Tomboy - a desktop note-taking application
Summary(pl.UTF-8):	Tomboy - aplikacja do notatek na pulpicie
Name:		tomboy
Version:	1.14.1
Release:	1
License:	LGPL v2.1
Group:		X11/Applications
Source0:	https://download.gnome.org/sources/tomboy/1.14/%{name}-%{version}.tar.xz
# Source0-md5:	969e7b48b19788899a410e9e757feba1
Patch0:		%{name}-dbus.patch
Patch1:		%{name}-cairo.patch
Patch2:		%{name}-make.patch
URL:		https://wiki.gnome.org/Apps/Tomboy
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	atk-devel >= 1:1.2.4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
#BuildRequires:	dotnet-galago-sharp-devel >= 0.5.0
BuildRequires:	dotnet-gconf-sharp-devel >= 2.24.0
BuildRequires:	dotnet-gmime-sharp-devel >= 2.6.0
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.2
BuildRequires:	dotnet-dbus-sharp-devel >= 0.8
BuildRequires:	dotnet-dbus-sharp-glib-devel >= 0.6
BuildRequires:	gettext-tools
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.17.3
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	gtkspell-devel >= 2.0.11
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	mono-addins-devel >= 0.3
BuildRequires:	mono-addins-gui-devel >= 0.3
BuildRequires:	mono-csharp >= 1.9.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 2.015
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	shared-mime-info
Requires(post,preun):	GConf2
Suggests:	galago-daemon
ExclusiveArch:	%{ix86} %{x8664} %{arm} hppa ppc s390 sparc sparcv9
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tomboy is a desktop note-taking application for Linux and Unix. Simple
and easy to use, but with potential to help you organize the ideas and
information you deal with every day.

%description -l pl.UTF-8
Tomboy to aplikacja do notatek na pulpicie dla Linuksa i Uniksa.
Prosta i łatwa w użyciu, ale z potencjałem pomocy przy organizacji
pomysłów i informacji, z którymi musimy się zmagać każdego dnia.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%{__sed} -i -e '1s,/usr/bin/env bash,/bin/bash,' Tomboy/tomboy.in

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	GMCS=/usr/bin/mcs \
	--with-dbus-service-dir="%{_datadir}/dbus-1/services" \
	--disable-galago \
	--disable-schemas-install \
	--disable-scrollkeeper \
	--disable-update-mimedb

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/%{name}/*.la

# not supported by glibc
%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/en@shaw

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install tomboy.schemas
%update_icon_cache hicolor
%update_mime_database

%preun
%gconf_schema_uninstall tomboy.schemas

%postun
%update_mime_database
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/tomboy
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.exe.config
%{_libdir}/%{name}/*.exe.mdb
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/addins
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/org.gnome.Tomboy.service
%{_datadir}/mime/packages/tomboy.xml
%{_sysconfdir}/gconf/schemas/tomboy.schemas
%{_desktopdir}/tomboy.desktop
%{_iconsdir}/hicolor/*/apps/tomboy.*
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-note.png
%{_mandir}/man1/tomboy.1*

# -devel?
%{_pkgconfigdir}/tomboy-addins.pc
