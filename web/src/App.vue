<template>
    <nav class="navbar navbar-dark bg-dark justify-content-center">
        <div class="nav nav-pills">
            <router-link class="text-center nav-link" :class="{ active : this.$route.name === 'All Articles' }" to="/articles">
                Show Articles
            </router-link>
            <router-link class="text-center nav-link" :class="{ active : this.$route.name === 'New Article' }" to="/articles/new">
                New Article
            </router-link>
        </div>
    </nav>
    <div class="container">
        <router-view :key="$route.path"/>
    </div>
</template>
