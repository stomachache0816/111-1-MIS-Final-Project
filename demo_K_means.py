import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from nltk.tokenize import TweetTokenizer

tokenizer = TweetTokenizer()

file = open('coordinates_data.txt', 'r')
line = file.readline()

x = []
y = []

while line != '':
    coordinate = tokenizer.tokenize(line)
    x.append(int(coordinate[0]))
    y.append(int(coordinate[1]))
    line = file.readline()

file.close()

data = list(zip(x, y))

fig1 = plt.figure()
fig1.set_size_inches(16, 9)
for n in range(1, 10 + 1):
    fig1.add_subplot(2, 5, n)
    kmeans = KMeans(n_clusters=n)
    kmeans.fit(data)
    plt.scatter(x, y, c=kmeans.labels_, s=5)
    centers = kmeans.cluster_centers_
    plt.scatter(centers[:, 0], centers[:, 1], c='red', s=100, marker='*')

plt.savefig('my_pic1.png')

fig2 = plt.figure()


all_inertia = []
for i in range(1, 10 + 1):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(data)
    all_inertia.append(kmeans.inertia_)

plt.plot(range(1, 10 + 1), all_inertia, marker='o')
plt.title('Elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('Inertia')
plt.savefig('my_pic2.png')
plt.show()
