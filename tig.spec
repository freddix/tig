Summary:	Text-mode interface for git
Name:		tig
Version:	2.1.1
Release:	1
License:	GPL v2
Group:		Development/Tools
Source0:	http://jonas.nitro.dk/tig/releases/%{name}-%{version}.tar.gz
# Source0-md5:	d6eb13d31319d57a3f726d8238f8ebc0
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
%{__aclocal} -I tools
%{__autoconf}
%{__autoheader}
%configure
%{__make} V=1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install-doc-man \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc *.html
%attr(755,root,root) %{_bindir}/tig
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/tigrc
%{_mandir}/man*/*.*

