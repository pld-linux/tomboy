#
%include	/usr/lib/rpm/macros.mono
#
Summary:	Tomboy - a desktop note-taking application
Summary(pl.UTF-8):	Tomboy - aplikacja do notatek na pulpicie
Name:		tomboy
Version:	1.8.3
Release:	0.1
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tomboy/1.8/%{name}-%{version}.tar.bz2
# Source0-md5:	760d343acc6a603ccaa1f50e4aac58af
URL:		http://www.gnome.org/projects/tomboy/
BuildRequires:	GConf2-devel >= 2.26.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	docbook-dtd412-xml
#BuildRequires:	dotnet-galago-sharp-devel >= 0.5.0
BuildRequires:	dotnet-gmime-sharp-devel >= 2.4.0
BuildRequires:	dotnet-gnome-desktop-sharp-devel >= 2.24.0
BuildRequires:	dotnet-gnome-sharp-devel >= 2.24.0
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.2
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel >= 0.3
BuildRequires:	dotnet-dbus-sharp-devel >= 0.4
BuildRequires:	dotnet-dbus-sharp-glib-devel >= 0.3
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gtk+2-devel >= 2:2.20.0
BuildRequires:	gtkspell-devel >= 2.0.11
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libtool
BuildRequires:	mono-addins-devel >= 0.3
BuildRequires:	mono-csharp >= 1.9.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
Requires(post,postun):	shared-mime-info
Requires(post,preun):	GConf2
Suggests:	galago-daemon
# sr@Latn vs. sr@latin
Conflicts:	glibc-misc < 6:2.7
ExclusiveArch:	%{ix86} %{x8664} alpha arm hppa ppc s390 sparc sparcv9
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

%{__sed} -i -e 's/en@shaw//' po/LINGUAS
rm -f po/en@shaw.po

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-dbus-service-dir="%{_datadir}/dbus-1/services" \
	--disable-update-mimedb \
	--disable-schemas-install \
	--disable-galago \
	--disable-scrollkeeper

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome --with-omf

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install tomboy.schemas
%scrollkeeper_update_post
%update_icon_cache hicolor
%update_mime_database

%preun
%gconf_schema_uninstall tomboy.schemas

%postun
%update_mime_database
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.exe.mdb
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/*.config
%{_libdir}/%{name}/addins
%{_datadir}/%{name}
%{_datadir}/dbus-1/services/*.service
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/tomboy.1*
%{_pkgconfigdir}/tomboy-addins.pc
%{_sysconfdir}/gconf/schemas/tomboy.schemas
%{_datadir}/mime/packages/tomboy.xml
