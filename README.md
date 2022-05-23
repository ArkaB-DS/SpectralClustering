# SpectralClustering

This repo contains the codes, images, report and slides for the project of the course - `MTH552A: Statistical & AI Techniques in Data Mining` at IIT Kanpur during the academic year 2022-2023.

## Project Title
`Spectral Clustering:  Theory and Applications` [`[Report]`](https://github.com/ArkaB-DS/SpectralClustering/blob/main/AI_Project.pdf)

## Abstract
> In this report, we present a class of  popular clustering algorithms called Spectral Clustering algorithms. We introduce graph theoretic notations required to understand the report. We discuss similarity graphs and graph Laplacians, along with their important properties. Three popular clustering algorithms are presented. Choice of optimal number of clusters, similarity functions, similarity  graphs and graph Laplacians are also discussed. We then present Spectral clustering through different looking glasses. Finally, we apply Spectral clustering to simulated and real life datasets. This report is primarily based on [1].

## Table of Content

|**Section**|**Topic**|
|-----------|---------|
|1|Introduction|
|2|Graph Theory: Some defintions and notations <ul>2.1 Clustering problem formulation based on graphs </ul> <ul>2.2 Notations </ul>|
|3|Similarity Graphs <ul>3.1 Construction <ul>3.1.1 Choice of similarity function </ul> <ul>3.1.2 Choice of similarity graph </ul> <ul>3.1.3 Choice of similarity graph parameters </ul></ul>|
|4|Graph Laplacian: Different types and their properties <ul> 4.1 The unnormlaized graph Laplacian</ul> <ul>4.2 The normlaized graph Laplacian </ul>|
|5|Three Spectral Clustering Algorithms|
|6|Choice of cluster number|
|7|Choice of graph Laplacian <ul>7.1 Clustering Objectives</ul> <ul>7.2 Asymptotics</ul>|
|8|Spectral Clustering: Different Points of view <ul> 8.1 Graph Cut point of view <ul>8.1.1 Approximating RatioCut for $k=2$ </ul> <ul>8.1.2 Approximating RatioCut for arbitrary k=2 </ul> <ul>8.1.3 Approximating NCut for $k=2$ </ul> <ul>8.1.4 Approximating NCut for arbitrary k </ul> </ul> <ul> 8.2 Random Walk point of view </ul>|
|9|Applications <ul>9.1 Synthetic Data <ul>9.1.1 k-means vs. Spectral Clustering </ul><ul>9.1.2 Image Segmentation</ul></ul> <ul>9.2 Real Data <ul>9.2.1 Iris dataset </ul></ul>|

  
## Primary Reference

  [1]. [Von Luxburg, Ulrike. "A tutorial on spectral clustering." Statistics and computing 17, no. 4 (2007): 395-416.](https://idp.springer.com/authorize/casa?redirect_uri=https://link.springer.com/content/pdf/10.1007/s11222-007-9033-z.pdf&casa_token=D38DQJHbX-MAAAAA:rsNOf6rDvoZtSZPJVeLIVAKHoIsjui8ZR_qrJl8LhEuursk8T-IuBfM4Ov_TA3u9Tik5ewUhTbuKiX0)
