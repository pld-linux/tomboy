Summary:	Tomboy - a desktop note-taking application
Summary(pl):	Tomboy - aplikacja do notatek na pulpicie
Name:		tomboy
Version:	0.3.3
Release:	2
License:	LGPL v2.1
Group:		X11/Applications
Source0:	http://www.beatniksoftware.com/tomboy/releases/%{name}-%{version}.tar.gz
# Source0-md5:	7ad987216b484f747f53aa7f9055a46b
Patch0:		%{name}-desktop.patch
URL:		http://www.beatniksoftware.com/tomboy/
BuildRequires:	GConf2-devel
BuildRequires:	atk-devel >= 1.2.4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-dbus-sharp-devel
BuildRequires:	dotnet-gtk-sharp-devel
BuildRequires:	dotnet-gtk-sharp-gnome-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	gtkspell-devel >= 2.0.5
BuildRequires:	intltool >= 0.25
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires:	mono
Requires:	dotnet-dbus-sharp
Requires:	dotnet-gtk-sharp
Requires:	dotnet-gtk-sharp-gnome
Requires:	gnome-panel
ExclusiveArch:	%{ix86} %{x8664} alpha arm hppa ppc s390 sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tomboy is a desktop note-taking application for Linux and Unix. Simple
and easy to use, but with potential to help you organize the ideas and
information you deal with every day.

%description -l pl
Tomboy to aplikacja do notatek na pulpicie dla Linuksa i Uniksa.
Prosta i ³atwa w u¿yciu, ale z potencja³em pomocy przy organizacji
pomys³ów i informacji, z którymi musimy siê zmagaæ ka¿dego dnia.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-schemas-install
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_datadir}/dbus-1/services}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp data/tomboy.desktop $RPM_BUILD_ROOT%{_desktopdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/dbus-1.0/services/*.service \
	$RPM_BUILD_ROOT%{_datadir}/dbus-1/services/

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install tomboy.schemas

%preun
%gconf_schema_uninstall tomboy.schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dbus-1/services/*.service
%{_datadir}/gnome-2.0/ui/*
%{_desktopdir}/*.desktop
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.config
%attr(755,root,root) %{_libdir}/%{name}/*.exe
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/Plugins
%{_libdir}/bonobo/servers/*
%{_mandir}/man1/tomboy.1*
%{_pixmapsdir}/*.png
%{_pkgconfigdir}/tomboy-plugins.pc
%{_sysconfdir}/gconf/schemas/tomboy.schemas
