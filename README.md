
### R函数式的列表(Lisp表达方式)

- [R函数式的列表(Lisp表达方式)](#r%E5%87%BD%E6%95%B0%E5%BC%8F%E7%9A%84%E5%88%97%E8%A1%A8lisp%E8%A1%A8%E8%BE%BE%E6%96%B9%E5%BC%8F)
    - [Emacs `C-x C-e` 执行R的S表达式](#emacs-c-x-c-e-%E6%89%A7%E8%A1%8Cr%E7%9A%84s%E8%A1%A8%E8%BE%BE%E5%BC%8F)
    - [lambda](#lambda)
    - [let](#let)
    - [if](#if)
    - [plot](#plot)
    - [Reduce](#reduce)
    - [Filter](#filter)
    - [Map](#map)
    - [vector](#vector)
    - [factor](#factor)
    - [list](#list)
    - [array](#array)
    - [data.frame (函数内赋值参数用: x=123)](#dataframe-%E5%87%BD%E6%95%B0%E5%86%85%E8%B5%8B%E5%80%BC%E5%8F%82%E6%95%B0%E7%94%A8-x123)
    - [matrix (函数内赋值参数用: x=123)](#matrix-%E5%87%BD%E6%95%B0%E5%86%85%E8%B5%8B%E5%80%BC%E5%8F%82%E6%95%B0%E7%94%A8-x123)
    - [csv 表格数据文件](#csv-%E8%A1%A8%E6%A0%BC%E6%95%B0%E6%8D%AE%E6%96%87%E4%BB%B6)
    - [table记录频数的方法(每一类)](#table%E8%AE%B0%E5%BD%95%E9%A2%91%E6%95%B0%E7%9A%84%E6%96%B9%E6%B3%95%E6%AF%8F%E4%B8%80%E7%B1%BB)
    - [round & prop.table & table计算频率百分比](#round--proptable--table%E8%AE%A1%E7%AE%97%E9%A2%91%E7%8E%87%E7%99%BE%E5%88%86%E6%AF%94)
    - [summary 总结数据特征,极值, 细胞核的3种特征: 最小, 最大, 平均值,中间值等](#summary-%E6%80%BB%E7%BB%93%E6%95%B0%E6%8D%AE%E7%89%B9%E5%BE%81%E6%9E%81%E5%80%BC-%E7%BB%86%E8%83%9E%E6%A0%B8%E7%9A%843%E7%A7%8D%E7%89%B9%E5%BE%81-%E6%9C%80%E5%B0%8F-%E6%9C%80%E5%A4%A7-%E5%B9%B3%E5%9D%87%E5%80%BC%E4%B8%AD%E9%97%B4%E5%80%BC%E7%AD%89)
    - [min & max 标准化数值型数据,以便确保在标准的范围内](#min--max-%E6%A0%87%E5%87%86%E5%8C%96%E6%95%B0%E5%80%BC%E5%9E%8B%E6%95%B0%E6%8D%AE%E4%BB%A5%E4%BE%BF%E7%A1%AE%E4%BF%9D%E5%9C%A8%E6%A0%87%E5%87%86%E7%9A%84%E8%8C%83%E5%9B%B4%E5%86%85)
    - [lapply表格数据每一个数据单元都执行某个操作: 相当于map了,结果变成了list列表](#lapply%E8%A1%A8%E6%A0%BC%E6%95%B0%E6%8D%AE%E6%AF%8F%E4%B8%80%E4%B8%AA%E6%95%B0%E6%8D%AE%E5%8D%95%E5%85%83%E9%83%BD%E6%89%A7%E8%A1%8C%E6%9F%90%E4%B8%AA%E6%93%8D%E4%BD%9C-%E7%9B%B8%E5%BD%93%E4%BA%8Emap%E4%BA%86%E7%BB%93%E6%9E%9C%E5%8F%98%E6%88%90%E4%BA%86list%E5%88%97%E8%A1%A8)
    - [一元线性回归](#%E4%B8%80%E5%85%83%E7%BA%BF%E6%80%A7%E5%9B%9E%E5%BD%92)
    - [knn](#knn)
    - [regression](#regression)
    - [bayes](#bayes)
    - [str 查看dataframe特征 & 类型 & 总数, 数据轮廓](#str-%E6%9F%A5%E7%9C%8Bdataframe%E7%89%B9%E5%BE%81--%E7%B1%BB%E5%9E%8B--%E6%80%BB%E6%95%B0-%E6%95%B0%E6%8D%AE%E8%BD%AE%E5%BB%93)
    - [summary总结某列数据的Min/Max,Median,Mean等](#summary%E6%80%BB%E7%BB%93%E6%9F%90%E5%88%97%E6%95%B0%E6%8D%AE%E7%9A%84minmaxmedianmean%E7%AD%89)
    - [head看数据前几个值,tail-log](#head%E7%9C%8B%E6%95%B0%E6%8D%AE%E5%89%8D%E5%87%A0%E4%B8%AA%E5%80%BCtail-log)
    - [评估模型的性能: gmodels/CrossTable](#%E8%AF%84%E4%BC%B0%E6%A8%A1%E5%9E%8B%E7%9A%84%E6%80%A7%E8%83%BD-gmodelscrosstable)
    - [c50决策树](#c50%E5%86%B3%E7%AD%96%E6%A0%91)
    - [neuralnet](#neuralnet)
    - [svm](#svm)
    - [kmeans](#kmeans)
    - [R宏%>%](#r宏)
    - [特征选择Boruta](#%e7%89%b9%e5%be%81%e9%80%89%e6%8b%a9Boruta)
    - [直方图hist](#%e7%9b%b4%e6%96%b9%e5%9b%behist)
    - [散点图pairs](#%e6%95%a3%e7%82%b9%e5%9b%bepairs)

##### Emacs `C-x C-e` 执行R的S表达式
* `el-get-install ESS `
* `C-c C-k` 打开R的Repl, `C-c C-l`eval当前文件缓冲到Repl里面
* `C-x C-e` fun r lisp!
```emacs-lisp
;; 将这里的配置放到启动脚本init.el或者是`.emacs`
(defun ess-eval-sexp (vis)
  (interactive "P")
  (save-excursion
    (backward-sexp)
    (let ((end (point)))
      (forward-sexp)
      (ess-eval-region (point) end vis "Eval sexp"))))
      
(add-hook 'ess-mode-hook (lambda () (define-key global-map (kbd "C-x C-e") 'ess-eval-sexp) ))
```

##### lambda
```r
# define
(function (y) (function (x) ('+' (x, y))))
# call
((function (x) x) (1)) #=> [1] 1
```
##### let
```r
## 用高阶函数 和 %>% 管道来 代替let, function(a=111,b=222,c=function(...){...} ) { ... }
## function的默认参数就是一个局部变量: function(a=1, b=2) <=> let[a 1 b 2]
((function (x, y=(function (i) ('*' (i, 2))) ) (y (x))) (2)) #=> [1] 4

## 用强大的函数管道
(library (magrittr))
((c (1, 2, 3)) %>% (function (x) (Map ((function (x) ('+' (x, 100))), x)))
    %>% (function (x) (Reduce ('+', x)) ) ) #=> [1] 306

## let复用前面的变量定义
((function (x, y=('*' (x, 2))) y) (100)) #=> [1] 200
## 综合例子: function里面的默认参数,当let来用,可以用前面定义的变量(x,y=x),但是不能覆盖前面定义的变量(x,x=1)
((function (y, x, mx=(as.matrix (x)), cx=(cbind (Intercept=1, mx)))
    ('%*%' (('%*%' ((solve ('%*%' ((t (cx)), cx))), (t (cx)))), y)) ) -> reg)

(reg (y=(launch$distress_ct), x=(launch [3])))
##                    [,1]
## Intercept    4.30158730
## temperature -0.05746032
```
##### if
```r
('if' (0, ('==' (1, 1)), ('==' (2, 1)))) #=> [1] FALSE
```
##### plot
```r
('plot' (('rnorm' (10)), ('rnorm' (10))))
# 加了额外的参数
('plot' (('rnorm' (10)), ('rnorm' (10)), ('=' (type, 'b'))))
```
##### Reduce
```r
(Reduce ('*', 1:10))
```
##### Filter
```r
((function (x) ('if' (('%%' (x, 2)), x, 0))) (2)) #=> [1] 0
# call
(Filter ((function (x) ('if' (('%%' (x, 2)), x, 0))), 1:10)) #=>  [1] 1 3 5 7 9
```
##### Map
```r
(Map ((function (x) ('+' (x, 100))), 1:3))
# =>
[[1]]
[1] 101
[[2]]
[1] 102
[[3]]
[1] 103
```
##### vector
```r
## 1d: 1维
# 如果本来是前缀的表达方式的函数,引号'c'可以省略,function除外必须加引号
(c (1, 1, 3)) #=> [1] 1 1 3
((c (1, 8, 3)) [2]) #=> [1] 8
('=' (defvar, (c ("A", "B", "C")))) #=> [1] "A" "B" "C"
```
##### factor
```r
# levels是不能重复出现的
(factor ((c ("1", "1", "3", "11", "9", "8")), ('=' (levels, (c ("A", "B", "C", "AA", "BB", "CC"))))))
#=>
[1] <NA> <NA> <NA> <NA> <NA> <NA>
Levels: A B C AA BB CC

### 替换一下数据名称,把B替换为"良性肿块" ==>> 因子的意义: 赋予跟多的标签的意义
('<-' (wbcd$diagnosis, (factor (wbcd$diagnosis, levels=(c ("B", "M")), labels=(c ("良性肿块", "恶性肿块"))))))
#=>
    diagnosis radius_mean texture_mean perimeter_mean area_mean smoothness_mean
1    恶性肿块      17.990        10.38         122.80    1001.0         0.11840
2    恶性肿块      20.570        17.77         132.90    1326.0         0.08474
21   良性肿块      13.080        15.71          85.63     520.0         0.10750
```
##### list
```r
## 1d: 1维
(list (11, "aa", FALSE))
#=>
[[1]]
[1] 11
[[2]]
[1] "aa"
[[3]]
[1] FALSE
```
##### array
```r
## nd: N维
(1:12) ##=> [1]  1  2  3  4  5  6  7  8  9 10 11 12
##class:  [1] "integer"

(array (1:12)) #=>class  [1] "array"
##=> [1]  1  2  3  4  5  6  7  8  9 10 11 12

(array (1:12, (c (2, 3, 2)))) #=>class  [1] "array"
##      [,1] [,2] [,3]
## [1,]    7    9   11
## [2,]    8   10   12
##
```
##### data.frame (函数内赋值参数用: x=123)
```r
## 2d: 2维
('=' (pt_data,
  (data.frame (
    ID=(c (11,12,13)),
    Name=(c ("Devin","Edward","Wenli")),
    Gender=(c ("M","M","F")),
    Birthdate=(c ("1984-12-29","1983-5-6","1986-8-8"))))))
#=>
  ID   Name Gender  Birthdate
1 11  Devin      M 1984-12-29
2 12 Edward      M   1983-5-6
3 13  Wenli      F   1986-8-8

## get:
(pt_data [1, 2]) #=> 第一行,第二列
[1] Devin
Levels: Devin Edward Wenli

(pt_data [,3]) #=> 只是第三列
[1] M M F
Levels: F M

((pt_data [-1]) [-2])
#=> 去除第一,然后再去除第二列
     Name  Birthdate
 1  Devin 1984-12-29
 2 Edward   1983-5-6
 3  Wenli   1986-8-8
 
(pt_data$Birthdate)
#=> 取某一列
[1] 1984-12-29 1983-5-6   1986-8-8
Levels: 1983-5-6 1984-12-29 1986-8-8

(pt_data [2:3])
# 取范围
    Name Gender
1  Devin      M
2 Edward      M
3  Wenli      F
```
##### matrix (函数内赋值参数用: x=123)
```r
## 2d: 2维
(matrix ((c (1, 2, 1, 3, 5, 8)), nrow=2)) 
#=>  2行->3列
     [,1] [,2] [,3]
[1,]    1    1    5
[2,]    2    3    8

(matrix ((c (1, 2, 1, 3, 5, 8)), ncol=2))
#=>
     [,1] [,2]
[1,]    1    3
[2,]    2    5
[3,]    1    8

(matrix ((c (1, 2, 4, 3)), ncol=1))
#=> 单列矩阵
     [,1]
[1,]    1
[2,]    2
[3,]    4
[4,]    3

(matrix ((c (1, 2, 4, 3)), nrow=1))
#=> 单行矩阵
     [,1] [,2] [,3] [,4]
[1,]    1    2    4    3

## =========== 矩阵线性代数
## 矩阵转置: 如果参数里面只有一个参数时,并且是函数调用的时候,可以省略参数标记的一对括号,如下=>
(t (matrix ((c (1, 2, 1, 3, 5, 8)), ncol=2)))
##      [,1] [,2]
## [1,]    1    3
## [2,]    2    5
## [3,]    1    8
## ==>>
##      [,1] [,2] [,3]
## [1,]    1    2    1
## [2,]    3    5    8

## 矩阵的标量运算
('*' (10, (matrix ((c (1, 2, 1, 3, 5, 8)), ncol=2))))
##      [,1] [,2]
## [1,]   10   30
## [2,]   20   50
## [3,]   10   80
## 

## 矩阵求和: 必须结构相同才能相加
('+' ((matrix ((c (9, 2, 3, 8, 1, 4)), ncol=2)),
  (matrix ((c (0, 3, 5, 3, 7, 2)), ncol=2))))
# A + B
##      [,1] [,2]
## [1,]    9    8
## [2,]    2    1
## [3,]    3    4
##      [,1] [,2]
## [1,]    0    3
## [2,]    3    7
## [3,]    5    2
## =======>>>>>
##      [,1] [,2]
## [1,]    9   11
## [2,]    5    8
## [3,]    8    6
## 

## 矩阵乘法: A的列数必须等于B的行数 <=> 列的加权求和
('%*%' ((matrix ((c (1, 4, 3, 0, 1, 2)), ncol=2)),
  (matrix ((c (7, 8)), ncol=1))))
# A * B
##      [,1]
## [1,]    7
## [2,]   36
## [3,]   37
## 

## 矩阵求逆: 必需是正方形的
(solve (matrix ((c (1, 4, 3, 0, 1, 2, 1, 6, 8)), ncol=3)))
##      [,1] [,2] [,3]
## [1,]    1    0    1
## [2,]    4    1    6
## [3,]    3    2    8
## ===>>>
##      [,1] [,2] [,3]
## [1,]   -4    2   -1
## [2,]  -14    5   -2
## [3,]    5   -2    1
## 

```
##### csv 表格数据文件
```r
(write.csv (pt_data, ('=' (file, "my-data-frame.csv"))))
# cat my-data-frame.csv #=>
"","ID","Name","Gender","Birthdate"
"1",11,"Devin","M","1984-12-29"
"2",12,"Edward","M","1983-5-6"
"3",13,"Wenli","F","1986-8-8"

(read.csv ("my-data-frame.csv"))
#=>
  X ID   Name Gender  Birthdate
1 1 11  Devin      M 1984-12-29
2 2 12 Edward      M   1983-5-6
3 3 13  Wenli      F   1986-8-8

# => read from web:
('<-' (wbcd, (read.csv ("http://127.0.0.1:8003/wisc_bc_data.csv", stringsAsFactors=FALSE))))
```

##### table记录频数的方法(每一类)
```r
(table (wbcd$diagnosis))
#   B   M  # B是良性肿块, B是恶性肿块
# 357 212 
```

##### round & prop.table & table计算频率百分比
```r
(round (('*' ((prop.table (table (wbcd$diagnosis))) ,100)), digits=1))
## 2.良性肿块 恶性肿块 
##     62.7     37.3   # 百分比计算
```

##### summary 总结数据特征,极值, 细胞核的3种特征: 最小, 最大, 平均值,中间值等
```r
## 3.总结特征, 细胞核的3种特征: 最小, 最大, 平均值,中间值等
(summary ((wbcd [(c ("radius_mean", "area_mean", "smoothness_mean"))])))
#=>
 radius_mean       area_mean      smoothness_mean
Min.   : 6.981   Min.   : 143.5   Min.   :0.05263
1st Qu.:11.700   1st Qu.: 420.3   1st Qu.:0.08637
Median :13.370   Median : 551.1   Median :0.09587
Mean   :14.127   Mean   : 654.9   Mean   :0.09636
3rd Qu.:15.780   3rd Qu.: 782.7   3rd Qu.:0.10530
Max.   :28.110   Max.   :2501.0   Max.   :0.16340

```
##### min & max 标准化数值型数据,以便确保在标准的范围内
```r
('<-' (normalize,
  (function (x)
    ('/' (('-' (x, (min (x)))),
      ('-' ((max (x)), (min (x)))))))))
      
(normalize ((c (10, 20, 30, 40, 50)))) #=>  [1] 0.00 0.25 0.50 0.75 1.00
```
##### lapply表格数据每一个数据单元都执行某个操作: 相当于map了,结果变成了list列表
```r
(lapply ((wbcd [2:31]), normalize))
#=>
$radius_mean
  [1] 0.52103744 0.64314449 0.60149557 0.21009040 0.62989256 0.25883856
...
$texture_mean
  [1] 0.02265810 0.27257355 0.39026040 0.36083869 0.15657761 0.20257017
...

('<-' (wbcd_n, (as.data.frame ((lapply ((wbcd [2:31]), normalize)))))) 
#=> list列表(可以不同类型): 重新变成data.frame
     radius_mean texture_mean perimeter_mean  area_mean smoothness_mean
 1    0.52103744   0.02265810     0.54598853 0.36373277      0.59375282
 2    0.64314449   0.27257355     0.61578329 0.50159067      0.28987993

```

##### 一元线性回归
```r
('<-' (x, 1:10))
#=> [1]  1  2  3  4  5  6  7  8  9 10
('<-' (y, ('+' (x, (rnorm (10, 0, 1))))))
#=> 
# [1] 0.4150231 1.9585418 1.7173466 3.2213521 4.0119051 4.8112887 5.7995432
# [8] 7.1943800 9.3619532 9.2997215
('<-' (fit, (lm (y ~ x))))
#=>
#  Call:
#  lm(formula = y ~ x)
#
#  Coefficients:
#  (Intercept)            x
#      -0.8111       1.0164

(summary (fit))
#  Call:
#  lm(formula = y ~ x)
#
#  Residuals:
#       Min       1Q   Median       3Q      Max 
#   0.52077 -0.42176 -0.08944  0.14898  1.02546 
#
#  Coefficients:
#              Estimate Std. Error t value Pr(>|t|) 
#  (Intercept) -0.81107    0.38014  -2.134   0.0654 .
#  x            1.01640    0.06126  16.590 1.76e-07 ***
#  ---
#  Signif. codes:  0 ‘***’ 0.001 ‘**’ 0.01 ‘*’ 0.05 ‘.’ 0.1 ‘ ’ 1
#
#  Residual standard error: 0.5565 on 8 degrees of freedom
#  Multiple R-squared:  0.9718,	Adjusted R-squared:  0.9682 
#  F-statistic: 275.2 on 1 and 8 DF,  p-value: 1.76e-07
#
```

##### [knn](./knn.R)

```r
(library (class))

('<-' (wbcd_test_pred, (knn (train=wbcd_train, test=wbcd_test, cl=wbcd_train_labels, k=21))))
# knn返回wbcd_test_pred因子向量,为测试数据集中的每一个案例返回一个预测标签

# 评估模型的性能
(library (gmodels))
(CrossTable (x=wbcd_test_labels, y=wbcd_test_pred, prop.chisq=FALSE))

```
##### [bayes](./bayes.R)
```r

```
##### str 查看dataframe特征 & 类型 & 总数, 数据轮廓
```r
(str (credit))
#=>
'data.frame':   1000 obs. of  21 variables:
 $ checking_balance    : Factor w/ 4 levels "< 0 DM","> 200 DM",..: 1 3 4 1 1 4 4 3 4 3 ...
 $ months_loan_duration: int  6 48 12 42 24 36 24 36 12 30 ...
 $ credit_history      : Factor w/ 5 levels "critical","delayed",..: 1 5 1 5 2 5 5 5 5 1 ...
 $ purpose             : Factor w/ 10 levels "business","car (new)",..: 8 8 5 6 2 5 6 3 8 2 ...
 $ amount              : int  1169 5951 2096 7882 4870 9055 2835 6948 3059 5234 ...
 $ savings_balance     : Factor w/ 5 levels "< 100 DM","> 1000 DM",..: 5 1 1 1 1 5 4 1 2 1 ...
 $ employment_length   : Factor w/ 5 levels "> 7 yrs","0 - 1 yrs",..: 1 3 4 4 3 3 1 3 4 5 ...
 $ installment_rate    : int  4 2 2 2 3 2 3 2 2 4 ...
 $ personal_status     : Factor w/ 4 levels "divorced male",..: 4 2 4 4 4 4 4 4 1 3 ...
 $ other_debtors       : Factor w/ 3 levels "co-applicant",..: 3 3 3 2 3 3 3 3 3 3 ...
 $ residence_history   : int  4 2 3 4 4 4 4 2 4 2 ...
 $ property            : Factor w/ 4 levels "building society savings",..: 3 3 3 1 4 4 1 2 3 2 ...
 $ age                 : int  67 22 49 45 53 35 53 35 61 28 ...
 $ installment_plan    : Factor w/ 3 levels "bank","none",..: 2 2 2 2 2 2 2 2 2 2 ...
 $ housing             : Factor w/ 3 levels "for free","own",..: 2 2 2 1 1 1 2 3 2 2 ...
 $ existing_credits    : int  2 1 1 1 2 1 1 1 1 2 ...
 $ default             : int  1 2 1 1 2 1 1 1 1 2 ...
 $ dependents          : int  1 1 2 2 2 2 1 1 1 1 ...
 $ telephone           : Factor w/ 2 levels "none","yes": 2 1 1 1 1 2 1 2 1 1 ...
 $ foreign_worker      : Factor w/ 2 levels "no","yes": 2 2 2 2 2 2 2 2 2 2 ...
 $ job                 : Factor w/ 4 levels "mangement self-employed",..: 2 2 4 2 2 4 2 1 4 1 ...
```
##### summary总结某列数据的Min/Max,Median,Mean等

```r
(summary (credit$months_loan_duration))
#=>
 Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
 4.0    12.0    18.0    20.9    24.0    72.0
```
##### head看数据前几个值,tail-log
```r
(head (credit_rand$amount))
#=>
[1] 2346 2030 1082 2631 3069 1333
```
##### 评估模型的性能: gmodels/CrossTable
```r
(library (gmodels))
(CrossTable (x=wbcd_test_labels, y=wbcd_test_pred, prop.chisq=FALSE))
##                       | wbcd_test_pred 
##      wbcd_test_labels |  良性肿块 |  恶性肿块 | Row Total | 
##      -----------------|-----------|-----------|-----------|
##              良性肿块 |        77 |         0 |        77 | 
##                       |     1.000 |     0.000 |     0.770 | 
##                       |     0.975 |     0.000 |           | 
##                       |     0.770 |     0.000 |           | 
##      -----------------|-----------|-----------|-----------|
##              恶性肿块 |         2 |        21 |        23 | 
##                       |     0.087 |     0.913 |     0.230 | 
##                       |     0.025 |     1.000 |           | 
##                       |     0.020 |     0.210 |           | 
##      -----------------|-----------|-----------|-----------|
##          Column Total |        79 |        21 |       100 | 
##                       |     0.790 |     0.210 |           | 
##      -----------------|-----------|-----------|-----------|
```

##### [c50决策树](./c50.R)

```r
(library (C50))
('<-' (credit_model, (C5.0 ((credit_train [-17]), credit_train$default))))
('<-' (credit_pred, (predict (credit_model, credit_test))))
(CrossTable (credit_test$default, credit_pred, prop.chisq=FALSE, prop.c=FALSE, prop.r=FALSE, dnn=(c ('actual default', 'predicted default'))))
```
##### [neuralnet](./neuralnet.R)
```r
(library (neuralnet))
## neuralnet函数用于数值预测的神经网络: 多种原料=>强度预测, 用多层前馈神经网络
('<-' (concrete_model, (neuralnet (strength ~ cement + slag + ash + water + superplastic + coarseagg + fineagg + age, data=concrete_train))))
## 预测强度
('<-' (predicted_strength, (model_results$net.result)))
## cor用来获取两个数值向量之间的相关性
(cor (predicted_strength, concrete_test$strength))
##              [,1]
## [1,] 0.7195218932
```
##### [svm](./ocr_svm.R)
```r
(library (kernlab))
## 字母分类器: 超平面分割面=>两类数据空间化(填充,龚起来)=>分割完了再降维
('<-' (letter_classifier, (ksvm (letter ~ ., data=letters_train, kernel="vanilladot"))))
## 评估模型的性能: 字母的预测
('<-' (letter_predictions, (predict (letter_classifier, letters_test))))

## 预测的值和真实的值进行比较=>
(round (('*' ((prop.table (table ('==' (letter_predictions, letters_test$letter)))) ,100)), digits=1))
## ==>> 正确率为83.9%
## FALSE  TRUE
##  16.1  83.9
```
##### [kmeans](./kmeans.R)
```r
## 只是取36个特征:
('<-' (interests, (teens [5:40])))
('<-' (interests_z, (as.data.frame (lapply (interests, scale)))))

## k均值聚类:
('<-' (teen_clusters, (kmeans (interests_z, 5))))

## 看到分出来5类,各自的数量如下
(teen_clusters$size)
# [1]   868  5089  2528   986 20529

# 分量teen_clusters$centers查看聚类质心的坐标,所有的特征
(teen_clusters$centers) 
```

##### R宏%>%
```r
(library (magrittr))
(1 %>% (function (x) ('+' (x, 100)))
    %>% (function (x) (print (x))) ) #=> [1] 101
```
* 对于function里面定义临时变量,用pipe
```r
(library (tm))
(library (magrittr))

('<-' (getTermMatrix, (function (text)
    (text
        %>% (function (st) (Corpus ((VectorSource (st)))))
        %>% (function (cor) (tm_map (cor, (content_transformer (tolower)))))
        %>% (function (cor) (tm_map (cor, removePunctuation)))
        %>% (function (cor) (tm_map (cor, removeNumbers)))
        %>% (function (cor) (tm_map (cor, removeWords, (c (stopwords("SMART"), "thy", "thou", "thee", "the", "and", "but")))))
        %>% (function (cor) (TermDocumentMatrix (cor, control=(list (minWordLength=1)))))
        %>% (function (mydtm) (as.matrix (mydtm)))
        %>% (function (m) (sort ((rowSums (m)), decreasing=TRUE))) ))))

(getTermMatrix ("The Clojure Programming Language. Clojure is a dynamic, general-purpose programming")) #=>
##        clojure    programming        dynamic generalpurpose       language
##              2              2              1              1              1

```

##### [regression](./regression.R)

```r
## 3.1 探索特征之间的关系---相关系数矩阵
(cor (insurance [(c ("age", "bmi", "children", "charges"))]))
##                age       bmi   children    charges
## age      1.0000000 0.1092719 0.04246900 0.29900819
## bmi      0.1092719 1.0000000 0.01275890 0.19834097
## children 0.0424690 0.0127589 1.00000000 0.06799823
## charges  0.2990082 0.1983410 0.06799823 1.00000000

## 3.2 可视化特征之间的关系------散点图矩阵
## (pairs (insurance [(c ("age", "bmi", "children", "charges"))])) #=> pairs_insurance.png
(library (psych)) ## pairs.panels可以显示拟合的线
## (pairs.panels (insurance [(c ("age", "bmi", "children", "charges"))])) #=> pairs_panels_insurance.png

## 3.3 基于数据训练模型 --------------
((lm (charges ~ age + children + bmi + sex + smoker + region, data=insurance)) -> ins_model)
## Call:
## lm(formula = charges ~ age + children + bmi + sex + smoker +
##     region, data = insurance)
##
## Coefficients:
##     (Intercept)              age         children              bmi
##        -11938.5            256.9            475.5            339.2
##         sexmale        smokeryes  regionnorthwest  regionsoutheast
##          -131.3          23848.5           -353.0          -1035.0
## regionsouthwest
##          -960.1
##

## 3.4 评估模型的性能
(summary (ins_model))
```
##### [特征选择Boruta](./Boruta_Feature_Selection.R)
* [Boruta Ozone, form library mlbench's data](./Boruta_Ozone.R)
* [Boruta Madelon](./Boruta_Madelon.R)
```r
(library (Boruta))
('<-' (Boruta.mod, (Boruta (Classes~., data=(train [,-348])))))
(png ("Boruta_selection.png", width=4000,height=1600))
(plot (Boruta.mod, las="2"))
(dev.off ())
## 将选出来的重要特征保存到一个rda里面
(library (magrittr))
(library (dplyr)) #select函数
(train %>%
 (function (data) (select (data, zakończyć,zdjęcie,należeć,naprawdę,polski,kobieta,sierpień,zobaczyć,dotyczyć,szczęście,mężczyzna,europejski)))
    -> train_Boruta)
(save (train_Boruta, file="train_Boruta.rda"))
```
##### 直方图hist
```r
(hist (insurance$charges)) #==>> charges_hist.png
```
##### 散点图pairs
```r
(pairs (insurance [(c ("age", "bmi", "children", "charges"))])) #=> pairs_insurance.png
```
