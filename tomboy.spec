#
%include	/usr/lib/rpm/macros.mono
#
Summary:	Tomboy - a desktop note-taking application
Summary(pl.UTF-8):	Tomboy - aplikacja do notatek na pulpicie
Name:		tomboy
Version:	0.12.1
Release:	2
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/GNOME/sources/tomboy/0.12/%{name}-%{version}.tar.bz2
# Source0-md5:	934d1258f855f04eff7d0fe8a976f6ad
URL:		http://www.gnome.org/projects/tomboy/
BuildRequires:	GConf2-devel >= 2.24.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.73
BuildRequires:	dotnet-galago-sharp-devel >= 0.5.0
BuildRequires:	dotnet-gmime22-sharp-devel >= 2.2.23
BuildRequires:	dotnet-gnome-desktop-sharp-devel >= 2.24.0
BuildRequires:	dotnet-gnome-sharp-devel >= 2.24.0
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.12.2
BuildRequires:	dotnet-ndesk-dbus-glib-sharp-devel >= 0.3
BuildRequires:	gettext-devel
BuildRequires:	gnome-common >= 2.24.0
BuildRequires:	gnome-doc-utils >= 0.14.0
BuildRequires:	gnome-panel-devel >= 2.24.0
BuildRequires:	gtk+2-devel >= 2:2.14.0
BuildRequires:	gtkspell-devel >= 2.0.11
BuildRequires:	intltool >= 0.40.0
BuildRequires:	libgnomeprintui-devel >= 2.18.1
BuildRequires:	libtool
BuildRequires:	mono-addins-devel >= 0.3
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(find_lang) >= 1.23
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,postun):	gtk+2
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
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

%build
%{__glib_gettextize}
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-dbus-service-dir="%{_datadir}/dbus-1/services" \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

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

%preun
%gconf_schema_uninstall tomboy.schemas

%postun
%scrollkeeper_update_postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_datadir}/%{name}
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.config
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/addins
%{_libdir}/bonobo/servers/*
%{_datadir}/dbus-1/services/*.service
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_mandir}/man1/tomboy.1*
%{_pkgconfigdir}/tomboy-addins.pc
%{_sysconfdir}/gconf/schemas/tomboy.schemas
