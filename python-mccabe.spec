#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	mccabe
Summary:	McCabe checker, plugin for flake8
Name:		python-%{module}
Version:	0.2.1
Release:	4
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/m/mccabe/mccabe-%{version}.tar.gz
# Source0-md5:	5a3f3fa6a4bad126c88aaaa7dab682f5
URL:		https://github.com/flintwork/mccabe
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-distribute
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-modules
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ned's script to check McCabe complexity.

%package -n python3-%{module}
Summary:	McCabe checker, plugin for flake8
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
Ned's script to check McCabe complexity.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}.py
%{py3_sitescriptdir}/__pycache__/%{module}.cpython-*.py[co]
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
