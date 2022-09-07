## Git Basic

**Git 기본 명령어**

----

ㅁ 깃허브 config 설정

git config --global user.name wolfy

git config --global user.email svstar94@naver.com



ㅁ 깃허브 config 삭제

//사용자 이름 설정하여 삭제
$git config --global --unset user.name 사용자이름
//전체 사용자 이름 삭제
$git config --global --unset-all user.name



//사용자 이메일 선택하여 삭제
$git config --global --unset user.email 사용자이메일
//전체 사용자 이메일 삭제
$git config --global --unset-all user.email



리스트 확인

$git config --global --list



----

### ㅇ 로컬 저장소 My Computer

#### ㅁ git init : 현재 Working Directory git으로 관리 선언

※ 프로젝트 단위로 git init 할 것 (상위에서 다시 git init X)

repository 하나씩 추가

```shell
$ git init
```

#### ㅁ git add 파일 or .(현재 폴더)

- git add : 깃 저장소에 등록
  - . 하위 디렉토리 전부

```shell
$ git add .
```

#### ㅁ git commit

- git commit : 깃 로그에 커밋

```shell
$ git commit -m "커밋 메시지"
```

#### ㅁ git log

- git log : git에 commit 내역 확인

```shell
$ git log
```

#### ㅁ git status

- git status : 현재 git 상태

```shell
$ git status
```

#### ㅁ git reset

- git reset HEAD . : add 취소
- git reset --option HEAD^ : commit 취소
  - --soft : add 상태로 전환
  - --mixed : Working Directory에 보존
  - --hard : Working Directory에서 삭제
  - HEAD~number : number 만큼 commit 취소

```shell
$ git reset HEAD
$ git reset --soft HEAD^
```

 

----



### ㅇ 원격저장소 GitHub

#### ㅁ git remote : GitHub에 연결

- add origin 주소 : GitHub 주소 설정
  - repository (.git 추가)

```shell
$ git remote add origin 주소.git
```

- remove origin : GitHub 주소 초기화

```shell
$ git remote remove origin
```

- -v origin 확인

```shell
$ git remote -v
```

#### ㅁ git push : GitHub에 등록

- git push origin master

```shell
$ git push origin master
```

#### ㅁ git pull : GitHub에서 처리되지 않은 Commit 불러오기

- git pull origin master

```shell
$ git pull origin master
```



----



## GitHub Cooperation

### ㅇ 협엽프로젝트 진행 시 깃허브 기반 프로젝트 관리 방법

#### ㅁ git clone : GitHub에서 프로젝트 복제 (1회만)

- git clone <origin>

``` shell
$ git clone origin
```

- git clone <origin>

``` shell
$ git clone -b {branch_name} --single-branch {origin}
```


#### ㅁ git branch: 협업 프로젝트용 branch 생성 (임시 add, commit)

- git branch <name>

``` shell
$ git branch sosin
```



#### ㅁ git checkout: 협업 프로젝트 branch로 전환 (임시 add, commit)

- git checkout <branch>
- git checkout -b <branch> 생성도 함께 진행

``` shell
$ git checkout sosin(master)
```



**개인 프로젝트 진행하듯이 동일하게 add, commit 작업 후 branch master로 전환**



#### ㅁ git fetch: 강제 버전 맞추기 1

- git fetch --all

```shell
$ git fetch --all
```

#### ㅁ git reset: 강제 버전 맞추기 2

- git reset --hard master

```shell
$ git reset --hard master
```



#### ㅁ git merge: 협업 프로젝트 commit 병합 

- git merge <commit code> (branch에서 git status에 commit log 확인하여 가져오기)

``` shell
$ git merge 6d6a6932ce4cfd18d48cfd5c3fa3cbd4546202bf
```



**push origin 원격저장소에 등록**









ㅁ [참고자료 (깃허브 강의)](https://backlog.com/git-tutorial/kr/)