Summary:	Text-mode interface for git
Name:		tig
Version:	2.0.2
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://jonas.nitro.dk/tig/releases/%{name}-%{version}.tar.gz
# Source0-md5:	e10e925d73d32ff7e17352b79dbc16f9
URL:		http://jonas.nitro.dk/tig/
BuildRequires:	ncurses-devel
BuildRequires:	readline-devel
Requires:	git
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tig is a git repository browser that additionally can act as a
pager for output from various git commands.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-doc-man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.html
%attr(755,root,root) %{_bindir}/tig
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tigrc
%{_mandir}/man*/*.*

