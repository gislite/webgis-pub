<template>
  <div id="center_fz8">

<h2>dfasdf</h2>


<video width="320" height="240" controls>
  <source src="http://r.osgeo.cn:8008/video/heitu/sanjiang2022.webm" type="video/mp4">
  

</video>

  </div>

</template>

<script>

</script>

<style lang="scss" scoped>

#center_fz8 {
  height: 95vh;

  .btn {
    &.activity {
      background: #7B68EE;
      border: #8A71AB 1px solid;
      color: #fff;
    }
  }

  input[type=checkbox].switch {
    margin-right: 5px;
    outline: none;
    appearance: none;
    -webkit-appearance: none;
    -moz-appearance: none;
    position: relative;
    width: 30px;
    height: 15px;
    border-radius: 15px;
    border: 1px solid #ccc;
    background-color: #ccc;
    top: 2px
  }

  input[type=checkbox].switch::after {
    content: '';
    display: inline-block;
    width: 15px;
    height: 14px;
    border-radius: 50%;
    background-color: #fff;
    box-shadow: 0 0 2px #999;
    transition: left 0.1s linear;
    position: absolute;
    top: 0;
    left: 0;
  }

  input[type=checkbox].switch:checked {
    background-color: #1ab394;
  }

  input[type=checkbox].switch:checked::after {
    position: absolute;
    top: 0;
    left: 50%;
  }


  .li_icon_yi {
    width: 100%;
    color: #fff;
    list-style: none;
  }

  .li_icon_yi:hover {
    cursor: pointer;
    color: #5cd9e8;
  }


  .text {
    color: #c3cbde;
  }

  .leaflet-popup-tip-container {
    background-color: rgba(255, 0, 0, 0.0);
    display: none;
  }

  .btn-sm {
    padding: 2px;
  }

  form {
    margin: .1rem;
    margin-top: .3rem;
    font-size: .18rem;
  }

  fieldset {

    label {
      font-size: 14px;
      margin: 10px 0;
      display: flex;

    }

    ul li {
      font-size: 14px;
    }
  }

  .icon_tab {
    margin-left: 15px;
  }
  .fonsize {
    font-size: 14px;
    color: #fff;
  }
}
</style>
