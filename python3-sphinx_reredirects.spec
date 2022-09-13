Summary:	Handle redirects for moved pages in Sphinx documentation projects
Summary(pl.UTF-8):	Obsługa przekierowań przeniesionych stron w projektach dokumentacji Sphinksa
Name:		python3-sphinx_reredirects
Version:	0.1.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-reredirects/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-reredirects/sphinx_reredirects-%{version}.tar.gz
# Source0-md5:	fec204611dc9c4b2bd8b997393104d88
URL:		https://pypi.org/project/sphinx-reredirects/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
sphinx-reredirects is the extension for Sphinx documentation projects
that handles redirects for moved pages. It generates HTML pages with
meta refresh redirects to the new page location to prevent 404 errors
if you rename or move your documents.

%description -l pl.UTF-8
sphinx-reredirects to rozszerzenie projektów dokumentacji Sphinksa,
obsługujące przekierowania dla przeniesionych stron. Generuje strony
HTML z nagłówkami przekierowującymi na nową lokalizację strony, aby
zapobiec błędom 404 w przypadku zmiany nazwy lub przeniesienia
dokumentu.

%prep
%setup -q -n sphinx_reredirects-%{version}

%{__sed} -i -e '/setup_requires=\["wheel"\]/d' setup.py

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/sphinx_reredirects
%{py3_sitescriptdir}/sphinx_reredirects-%{version}-py*.egg-info
