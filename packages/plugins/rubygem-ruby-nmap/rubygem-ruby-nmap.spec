# Generated from ruby-nmap-0.9.3.gem by gem2rpm -*- rpm-spec -*-
# template: scl
%{?scl:%scl_package rubygem-%{gem_name}}
%{!?scl:%global pkg_name %{name}}

%global gem_name ruby-nmap

Name: %{?scl_prefix}rubygem-%{gem_name}
Version: 0.9.3
Release: 4%{?dist}
Summary: A Ruby interface to Nmap
Group: Development/Languages
License: MIT
URL: https://github.com/sophsec/ruby-nmap#readme
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem

# start generated dependencies
Requires: %{?scl_prefix_ruby}ruby(release)
Requires: %{?scl_prefix_ruby}ruby >= 2.0.0
Requires: %{?scl_prefix_ruby}ruby(rubygems) >= 2.0.0
Requires: %{?scl_prefix}rubygem(nokogiri) >= 1.3
Requires: %{?scl_prefix}rubygem(nokogiri) < 2
Requires: %{?scl_prefix}rubygem(rprogram) >= 0.3
Requires: %{?scl_prefix}rubygem(rprogram) < 1
BuildRequires: %{?scl_prefix_ruby}ruby(release)
BuildRequires: %{?scl_prefix_ruby}ruby >= 2.0.0
BuildRequires: %{?scl_prefix_ruby}rubygems-devel >= 2.0.0
BuildArch: noarch
Provides: %{?scl_prefix}rubygem(%{gem_name}) = %{version}
# end generated dependencies

%description
A Ruby interface to Nmap, the exploration tool and security / port scanner.


%package doc
Summary: Documentation for %{pkg_name}
Group: Documentation
Requires: %{?scl_prefix}%{pkg_name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{pkg_name}.

%prep
%{?scl:scl enable %{scl} - << \EOF}
gem unpack %{SOURCE0}
%{?scl:EOF}

%setup -q -D -T -n  %{gem_name}-%{version}

%{?scl:scl enable %{scl} - << \EOF}
gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec
%{?scl:EOF}

%build
# Create the gem as gem install only works on a gem file
%{?scl:scl enable %{scl} - << \EOF}
gem build %{gem_name}.gemspec
%{?scl:EOF}

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%{?scl:scl enable %{scl} - << \EOF}
%gem_install
%{?scl:EOF}

%install
mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/.travis.yml
%exclude %{gem_instdir}/.yardopts
%license %{gem_instdir}/LICENSE.txt
%{gem_instdir}/gemspec.yml
%{gem_libdir}
%exclude %{gem_instdir}/ruby-nmap.gemspec
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/.document
%exclude %{gem_instdir}/.rspec
%doc %{gem_instdir}/ChangeLog.md
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/spec

%changelog
* Tue Apr 06 2021 Eric D. Helms <ericdhelms@gmail.com> - 0.9.3-4
- Rebuild for Ruby 2.7

* Fri Jan 17 2020 Zach Huntington-Meath <zhunting@redhat.com> - 0.9.3-3
- Update spec to remove the ror scl

* Tue Jan 07 2020 Eric D. Helms <ericdhelms@gmail.com> - 0.9.3-2
- Build for SCL

* Thu Jul 19 2018 Dirk Goetz <dirk.goetz@netways.de> 0.9.3-1
- Add rubygem-ruby-nmap generated by gem2rpm using the scl template
