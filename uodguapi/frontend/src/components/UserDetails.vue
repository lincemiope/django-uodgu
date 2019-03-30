<template lang="html">
  <div class="user-details">
      <b-card class="mt-2">
          <b-card-header>{{ user.username }}</b-card-header>
          <b-card-body>
              <b-row>
                  <b-col md="3"></b-col>
                  <b-col md="6">
                      <label for="input-alias">PG</label>
                      <b-form-input
                  </b-col>
              </b-row>
          </b-card-body>
      </b-card>
  </div>
</template>

<script>
import { apiService } from "../common/api.service";
export default {
    name: 'user-details',
    props: {
        user: {
            type: Object,
            default: null
        }
    },
    methods: {
        async updateUser() {
            await apiService('/api/user/', 'PUT', this.user)
            .then(result => {
                console.log(result);
            });
        }
    }
}
</script>

<style lang="css" scoped>
</style>
