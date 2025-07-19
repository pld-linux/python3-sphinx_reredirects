# TODO: finish doc
#
# Conditional build:
%bcond_with	doc	# Sphinx documentation (TODO)
%bcond_with	tests	# unit tests (use network)

Summary:	Handle redirects for moved pages in Sphinx documentation projects
Summary(pl.UTF-8):	Obsługa przekierowań przeniesionych stron w projektach dokumentacji Sphinksa
Name:		python3-sphinx_reredirects
Version:	1.0.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx-reredirects/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx-reredirects/sphinx_reredirects-%{version}.tar.gz
# Source0-md5:	235c5f317ce69012d934b97decf64f3f
URL:		https://pypi.org/project/sphinx-reredirects/
BuildRequires:	python3-build
BuildRequires:	python3-flit_core >= 3.2
BuildRequires:	python3-flit_core < 4
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.11
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-Sphinx >= 7.4
BuildRequires:	python3-pytest >= 8.3.5
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	sed >= 4.0
%if %{with doc}
BuildRequires:	python3-myst_parser >= 4.0.0
BuildRequires:	python3-linkify_it_py >= 2.0.3
BuildRequires:	python3-sphinx_copybutton >= 0.5.2
BuildRequires:	python3-sphinx_design >= 0.6.1
BuildRequires:	python3-sphinx_sitemap >=2.6.0
BuildRequires:	python3-sphinxcontrib-mermaid >= 1.0.0
BuildRequires:	sphinx-pdg-3 >= 8.1
%endif
Requires:	python3-modules >= 1:3.11
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

%build
%py3_build_pyproject

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%if %{with doc}
sphinx-build-3 -b html docs docs/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{py3_sitescriptdir}/sphinx_reredirects
%{py3_sitescriptdir}/sphinx_reredirects-%{version}.dist-info
