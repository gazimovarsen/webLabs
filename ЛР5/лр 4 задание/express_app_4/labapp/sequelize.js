/* 
Модуль инициализации подключения к БД
*/

const Sequelize = require('sequelize');   // подключаем пакет sequalize

// Подключение к БД SQLite
const dbcontext = new Sequelize({
  dialect: "sqlite",
  storage: "appdb.sqlite"
});

// Экспорт подключения к БД для использования в других модулях
module.exports = {
    dbcontext
}