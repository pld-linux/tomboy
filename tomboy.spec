Summary:	Tomboy - a desktop note-taking application
Summary(pl):	Tomboy - aplikacja do notatek na pulpicie
Name:		tomboy
Version:	0.3.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.beatniksoftware.com/tomboy/releases/%{name}-%{version}.tar.gz
# Source0-md5:	5011568beecbdd20768590470613fc9f
Source1:	%{name}.desktop
#Patch0:		%{name}-desktop.patch
URL:		http://www.beatniksoftware.com/tomboy/
BuildRequires:	GConf2-devel
BuildRequires:	atk-devel >= 1.2.4
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dotnet-dbus-sharp-devel
BuildRequires:	dotnet-gtk-sharp-devel
BuildRequires:	gtkspell-devel >= 2.0.5
BuildRequires:	gnome-panel-devel
BuildRequires:	intltool >= 0.25
BuildRequires:	libtool
BuildRequires:	mono-csharp
BuildRequires:	pkgconfig
Requires(post):	GConf2
Requires:	mono
Requires:	dotnet-gtk-sharp
Requires:	dotnet-dbus-sharp
Requires:	gnome-panel
ExclusiveArch:	%{ix86} amd64 arm hppa ppc s390 sparc sparcv9 sparc64
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
#%patch0 -p1

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
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install
/usr/bin/scrollkeeper-update

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/gconf/schemas/*.schemas
%{_libdir}/dbus-1.0/services/*.service
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/*.exe
%{_libdir}/%{name}/*.config
%attr(755,root,root) %{_libdir}/%{name}/*.so
%{_libdir}/%{name}/*.la
%dir %{_libdir}/%{name}/Plugins
%{_libdir}/%{name}/Plugins/*.dll
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_desktopdir}/*.desktop
%{_mandir}/man1/tomboy.1*
%{_pixmapsdir}/*.png
