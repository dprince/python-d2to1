%global with_python3 0
%global upname d2to1

Name: python-%{upname}
Version: 0.2.7
Release: 1%{?dist}
Summary: Allows using distutils2-like setup.cfg files with setup.py
License: BSD

Group: Development/Languages
URL: http://pypi.python.org/pypi/d2to1
Source0: http://pypi.python.org/packages/source/d/d2to1/%{upname}-%{version}.tar.gz
BuildRequires: python-devel python-setuptools
Requires: python-setuptools

BuildArch: noarch
%if 0%{?with_python3}
BuildRequires:  python3-devel python3-setuptools
Requires:  python3-setuptools
%endif # if with_python3

%description
d2to1 allows using distutils2-like setup.cfg files for a package's metadata 
with a distribute/setuptools setup.py script. It works by providing a 
distutils2-formatted setup.cfg file containing all of a package's metadata, 
and a very minimal setup.py which will slurp its arguments from the setup.cfg.

%if 0%{?with_python3}
%package -n python3-d2to1
Summary: Allows using distutils2-like setup.cfg files with setup.py

%description -n python3-d2to1
d2to1 allows using distutils2-like setup.cfg files for a package's metadata 
with a distribute/setuptools setup.py script. It works by providing a 
distutils2-formatted setup.cfg file containing all of a package's metadata, 
and a very minimal setup.py which will slurp its arguments from the setup.cfg.
%endif # with_python3

%prep
%setup -q -n %{upname}-%{version}
rm -rf %{upname}.egg-info

%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif # with_python3

find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python}|'

%build
%{__python} setup.py build

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
rm -rf %{buildroot}

%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install -O1 --skip-build --root  %{buildroot}
popd
%endif # with_python3

%{__python} setup.py install -O1 --skip-build --root  %{buildroot}

%files
%doc LICENSE README.rst
%{python_sitelib}/*

%if 0%{?with_python3}
%files -n python3-d2to1
%doc LICENSE README.rst
%{python3_sitelib}/*
%endif # with_python3


%changelog
* Wed Sep 26 2012 Sergio Pascual <sergiopr at fedoraproject.org> - 0.2.7-1
- New upstream source
- Removing upstream egg-info and defattr

* Thu Sep 22 2011 Sergio Pascual <sergiopr at fedoraproject.org> - 0.2.5-1
- Initial spec file

