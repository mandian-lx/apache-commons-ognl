%{?_javapackages_macros:%_javapackages_macros}
%global short_name commons-ognl

Name:           apache-%{short_name}
Version:        3.0.2
Release:        6.20120313svn1102435.0%{?dist}
Summary:        Object Graph Navigation Library


License:        ASL 2.0
URL:            http://commons.apache.org/ognl/
# svn export -r1102435 http://svn.apache.org/repos/asf/commons/proper/ognl/trunk/ apache-commons-ognl-3.0.2
# tar caf apache-commons-ognl-3.0.2.tar.xz apache-commons-ognl-3.0.2
Source0:        %{name}-%{version}.tar.xz
BuildArch:      noarch

BuildRequires: java-devel
BuildRequires: jpackage-utils    
BuildRequires: maven-local
BuildRequires: javassist
BuildRequires: jna

%description
OGNL is an expression language for getting and setting properties of
Java objects, plus other extras such as list projection and selection
and lambda expressions.

%package javadoc
Summary:      API documentation for %{name}


%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q

%mvn_file :%{short_name} %{short_name} %{name}

%build
%mvn_build

%install
%mvn_install
%if 0%{?fedora}
%else
sed -i "s|4.0-incubating-SNAPSHOT|4.0.incubating.SNAPSHOT|" %{buildroot}%{_mavendepmapfragdir}/*
%endif

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt

%changelog
* Sun Aug 11 2013 Mat Booth <fedora@matbooth.co.uk> - 3.0.2-6.20120313svn1102435
- Update for newer guidelines

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-5.20120313svn1102435
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-4.20120313svn1102435
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 3.0.2-3.20120313svn1102435
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0.2-2.20120313svn1102435
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 13 2012 Andy Grimm <agrimm@gmail.com> - 3.0.2-1.20120313svn1102435
- Rename and reversion package
- add jna as a BuildRequires

* Fri Feb 17 2012 Andy Grimm <agrimm@gmail.com> - 3.0.2-1
- Initial package
