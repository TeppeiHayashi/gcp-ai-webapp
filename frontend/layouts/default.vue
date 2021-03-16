<template>
  <v-app>
    <!-- SideMenu　START -->
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list>
        <v-list-group
          v-for="item in items"
          :key="item.title"
          v-model="item.active"
          :prepend-icon="item.icon"
          no-action
        >
          <template #activator>
            <v-list-item-content>
              <v-list-item-title v-text="item.title" />
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="child in item.items"
            :key="child.title"
            :to="`${item.to}${child.to}`"
          >
            <v-list-item-content>
              <v-list-item-title v-text="child.title" />
            </v-list-item-content>
          </v-list-item>
        </v-list-group>
      </v-list>
    </v-navigation-drawer>
    <!-- SideMenu　END -->

    <!-- Header START -->
    <v-app-bar app>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer" />

      <v-toolbar-title v-text="title" />
    </v-app-bar>
    <!-- Header END -->

    <!-- Main Start -->
    <v-main>
      <v-container>
        <nuxt />
      </v-container>
    </v-main>
    <!-- Main END -->

    <!-- Footer START -->
    <v-footer
      app
    >
      <span>&copy; {{ new Date().getFullYear() }}</span>
    </v-footer>
    <!-- Footer END -->
  </v-app>
</template>

<script>
export default {
  data () {
    return {
      drawer: true,
      items: [
        {
          icon: 'mdi-camera',
          title: '画像認識',
          to: '/vision',
          items: [
            {
              title: '物体抽出',
              to: '/object-localization'
            },
            {
              title: '文字列抽出',
              to: '/text-detection'
            }
          ]
        },
        {
          icon: 'mdi-web',
          title: '自然言語',
          to: '/natural-language',
          items: [
            {
              title: '感情分析',
              to: '/analyze-sentiment'
            },
            {
              title: 'エンティティ分析',
              to: '/analyze-entities'
            }
          ]
        }
      ],
      title: 'GCP Web APP'
    }
  }
}
</script>
