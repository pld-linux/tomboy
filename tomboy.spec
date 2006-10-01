#
%include	/usr/lib/rpm/macros.mono
#
Summary:	Tomboy - a desktop note-taking application
Summary(pl):	Tomboy - aplikacja do notatek na pulpicie
Name:		tomboy
Version:	0.4.1
Release:	1
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://ftp.gnome.org/pub/gnome/sources/tomboy/0.4/%{name}-%{version}.tar.bz2
# Source0-md5:	40e0f51d832d04f762851fc9a88c01ea
Patch0:		%{name}-desktop.patch
URL:		http://www.beatniksoftware.com/tomboy/
BuildRequires:	GConf2-devel >= 2.14.0
BuildRequires:	atk-devel >= 1:1.12.2
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.71
BuildRequires:	dotnet-galago-sharp-devel >= 0.5.0
BuildRequires:	dotnet-gnome-sharp-devel >= 2.16.0
BuildRequires:	dotnet-gmime-sharp-devel >= 2.2.3
BuildRequires:	dotnet-gtk-sharp2-devel >= 2.10.0
BuildRequires:	gnome-panel-devel >= 2.16.0
BuildRequires:	gtkspell-devel >= 2.0.11
BuildRequires:	intltool >= 0.35
BuildRequires:	libgnomeprintui-devel >= 2.12.1
BuildRequires:	libtool
BuildRequires:	mono-csharp >= 1.1.16.1
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	scrollkeeper
Requires(post,preun):	GConf2 >= 2.14.0
Requires(post,postun):	gtk+2 >= 2:2.10.3
Requires(post,postun):	hicolor-icon-theme
Requires(post,postun):	scrollkeeper
ExclusiveArch:	%{ix86} %{x8664} alpha arm hppa ppc s390 sparc sparcv9 sparc64
ExcludeArch:	i386
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tomboy is a desktop note-taking application for Linux and Unix. Simple
and easy to use, but with potential to help you organize the ideas and
information you deal with every day.

%description -l pl
Tomboy to aplikacja do notatek na pulpicie dla Linuksa i Uniksa.
Prosta i �atwa w u�yciu, ale z potencja�em pomocy przy organizacji
pomys��w i informacji, z kt�rymi musimy si� zmaga� ka�dego dnia.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-scrollkeeper
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	dbusservicedir="%{_datadir}/dbus-1/services"

%find_lang %{name} --with-gnome

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
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.config
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/Plugins
%{_libdir}/bonobo/servers/*

%{_datadir}/dbus-1/services/*.service
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/*
%{_pixmapsdir}/*.png
%{_mandir}/man1/tomboy.1*
%dir %{_omf_dest_dir}/%{name}
%{_omf_dest_dir}/%{name}/tomboy-C.omf
%lang(es) %{_omf_dest_dir}/%{name}/tomboy-es.omf
%lang(sv) %{_omf_dest_dir}/%{name}/tomboy-sv.omf
%{_pkgconfigdir}/tomboy-plugins.pc
%{_sysconfdir}/gconf/schemas/tomboy.schemas
