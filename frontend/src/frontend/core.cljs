(ns frontend.core
    (:require [reagent.core    :as r]
              [frontend.navbar :as n]))

(defn home-page []
  [n/navbar])

(defn mount-root []
  (r/render [home-page] (.getElementById js/document "app")))

(defn init! []
  (mount-root))
