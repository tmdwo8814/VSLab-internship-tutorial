# An Introduction to Digital Image Processing with Matlab

### Basic MATLAB

- it's pythonic(Numpy)

<br>

```
    *how to make array in  MATLAB*
    a = [4 -2 -4 7;1 5 -3 2;6 -8 -5 -6;-7 3 0 1]

    *result*
    4    -2    -4     7
    1     5    -3     2
    6    -8    -5    -6
    -7     3     0     1

    *access*
    a(2, 1:3)

    ans = 6 -8 -5

```
<br>

## Bit plane

- grey image의 각 픽셀은 8bit로 구성

<br>

**0000 0000(0) ~ 1111 1111(255)**

이 구성에서 첫 번째 비트가 1이면 픽셀의 최소값는은 128이므로 7번째 비트보다 이미지에 훨씬 중요한 영향을 준다

-> 첫번째 비트 : **Most Significant bit**

-> 마지막 비트 : **Least significant bit**

<br>

## Histogram Equalization(stretching)

- 이미지 밝기의 분포를 균일화

<br>

**histogram** in Image Processing
-> 이미지에서 특성(0~255)의 분포를 도표로 나타낸 것

**Histogram Equalization** : 히스토그램을 균일하게 하는 것

<br>

## Noise

<br>


1. **salt & pepper Noise** (impulse, shot, binary)
- 갑작스런 교란 신호로 인한, sharp한 노이즈
<br>
-> Low pass filtering, Median filtering으로 해결

<br>

2. **Gaussian Noise**
- 가장 일반적인 노이즈
<br>
-> image averaging, average filtering, wiener filtering

<br>

**Image averaging**

idea : 인공위성이나 현미경검사 같은 같은 이미지를 많이 수집 할 수 있는 경우 모든 이미지의 평균을 구하여 노이즈를 없애는 방법

<br>

**average filtering**

idea
Guass.Noise의 평균이 0인 상황에서의 averaging은 image의 blur 현상을 일으킬 수 있다. original blurred 현상 을 막기 위해 filter size의 trade-off가 필요하다.

```
*위 문제를 해결할 수 있는 MATLAB의 METHOD*

a3 = fspecial('average')
a5 = fspecial('average', [5,5])
tg3 = filter2(a3,t_ga)
tg5 = filter2(a5,t_ga)
```

<br>

## Edges

- 영상의 가장자리, 윤곽선을 다루는 분야

1. step edge
2. ramp edge
3. line edge
4. roof edge

-> 엣지의 여러 형태들

<br>

```
# Horizontal 특징 강화 필터
1   1   1
0   0   0
-1 - 1  -1

# vertical 특징 강화 필터
1 0 -1
1 0 -1
1 0 -1
```
**filter** : Prewitt, Sobel, Roberts..

<br>

**Laplacian Filter**

- 각 인덱스의 합이 0
- 중앙 인덱스의 주파수가 확 튐

-> 이미지의 검출 특성(edge) 증가
-> 노이즈에 민감

```
-1 -1 -1
-1 8  -1
-1 -1 -1
```

<br>

**Edge enhancement**

- Unsharp masking
- High boost filtering
 
<br>

**Unsharp masking process**

Origin image : M, blurred origin image : N

-> **M - k*N**

<br>

## Hough Transform

- image에서 strongest line(원, 직선)을 찾는 변환 방법

<br>

**IDEA**

- xy 평면의 y = ax + b 직선상의 점들을 ab평면으로 mapping
- ab평면의 직선들의 교점을 구한 뒤 xy 평면의 직선(strongest line)을 구한다

```
1.
(1,0) -> b = -a
(1,1) -> b = -a + 1
(2,1) -> b = -2a + 1
(4,1) -> b = -4a + 1
(3,2) -> b = -3a + 2

2. 
line들을 ab 평면에 투영 후 교점(a, b)찾기
(a, b) = (1, 0), (1, -1)

3. 
strongest line
y = x,
y = x -1
```






