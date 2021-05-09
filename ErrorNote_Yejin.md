# Troble shooting

##### [c:\OpenAPI\khopenapi.ocx] 파일 삭제 실패 [183]  [c:\OpenAPI\opcomms.dll] 파일 삭제 실패 [183]

- API 관련 모든 프로그램 종료 후, C:\OpenAPI 에서 'OPVersionUp' 실행 후 다시 작업.



##### twisted 18.7.0 requires PyHamcrest&gt;=1.9.0, which is not installed.

- pip install PyHamcrest==1.9.0



##### Cannot uninstall 'wrapt'. It is a distutils installed project and thus we cannot accurately determine which files belong to it which would lead to only a partial uninstall

- pip install --ignore tensorflow==1.15



##### NotImplementedError: Cannot convert a symbolic Tensor to a numpy array

- numpy 버전을 확인해보고 맞는 버전으로 재 다운로드한다, 주로 numpy 1.20 일때 발생하는 오류이다.

