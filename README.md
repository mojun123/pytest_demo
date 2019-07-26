# supplyAutoUITest

      框架主要功能
            -  动态生成目录及指定文件
            -  解析配置文件
            -  解析Excel表格文件
            -  记录日志
            -  生成Html测试报告
      项目框架
          python + selenium  + unittest
      
      需要用到得第三方库
          1.selenium
          2.HTMLTestRunner
          3.openpyxl
          
      目录结果
      - config
          -  存放整个项目所需要的配置文件
          -  存放页面元素
      -data 
          -  存放自动化测试用例需要的测试数据文件
      -package
          -  存放生成测试报告的第三方库
      -report
          -  存放测试报告和日志的地方
      -testcase
          -  models
            - 存放与业务无关公共方法的地方
          -  page
            - 重新封装的一些seleniumApi使用方法
          -  page_object
            - 存放待测试页面的一些需要用的方法
          - 写测试用例列
      -  跑测试用例的文件