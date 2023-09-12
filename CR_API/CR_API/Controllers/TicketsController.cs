using CR_API.Models;
using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Data.SqlClient;
using System.Globalization;
using System.Linq;
using System.Net;
using System.Net.Http;
using System.Reflection;
using System.Web.Http;


namespace CR_API.Controllers
{
    public class TicketsController : ApiController
    {
        public string Sess = "16FC6B61-3D5D-4DC5-8FBD-013FC42802C9";
        [Route("api/tickets/getall")]
        [HttpGet]
        public IEnumerable<Ticket> GetAll()
        {
            using (QAOrgEntities dbContext = new QAOrgEntities())
            {
                return dbContext.Ticket.ToList();
            }
        }

        [Route("api/tickets/get/{id}")]
        [HttpGet]
        public Ticket Get(int id)
        {
            using (QAOrgEntities dbContext = new QAOrgEntities())
            {
                return dbContext.Ticket.FirstOrDefault(e => e.TicketID == id);
            }
        }

        [Route("api/tickets/BuildTicket/{buildid}")]
        [HttpGet]
        public IEnumerable<ws_Build_Ticket_InBuild_Get_Result> BuildTicket(int buildid)
        {
            
            using (QAOrgEntities dBContext = new QAOrgEntities())
            {
                List<ws_Build_Ticket_InBuild_Get_Result> tickets = new List<ws_Build_Ticket_InBuild_Get_Result>();
                
                tickets = dBContext.ws_Build_Ticket_InBuild_Get(Sess, buildid, 0).ToList();

                return tickets;
            }
        }
        #region Xử lý list tuần

        //Lấy danh sách các tuần
        [Route("api/tickets/listweek/getallweek")]
        [HttpGet]
        public IEnumerable<Ticket_Week> GetAllWeek()
        {
            using (QAOrgEntities dbContext = new QAOrgEntities())
            {
                return dbContext.Ticket_Week.ToList();
            }
        }

        //Lấy danh sách team
        [Route("api/tickets/listweek/getallteam")]
        [HttpGet]
        public DataTable GetAllTeam()
        {
            using (QAOrgEntities dbContext = new QAOrgEntities())
            {
                List<L_Teams> lsst = new List<L_Teams>();
                lsst = dbContext.L_Teams.ToList();

                DataTable tb = new DataTable();
                tb = ToDataTable(lsst);
                var row = tb.NewRow();
                row["TeamID"] = 0;
                row["TeamName"] = "Tất cả";
                row["CreatedOn"] = null;
                row["CreatedBy"] = null;
                row["ModifiedOn"] = null;
                row["ModifiedBy"] = null;
                tb.Rows.InsertAt(row, 0);

                return tb;
            }
        }

        //Lấy danh sách list ticket tuần theo filter
        [Route("api/tickets/listweek/getlistweek")]
        [HttpGet]
        public IEnumerable<ws_Ticket_InWeek_List_Result> GetListWeek([FromUri] int weekid, [FromUri] int teamid)
        {
            using (QAOrgEntities dbContext = new QAOrgEntities())
            {
                var ticketWeek = dbContext.ws_Ticket_InWeek_List(Sess,weekid, teamid).ToList();
                return ticketWeek;                    
            }
        }
        public DataTable ToDataTable<T>(List<T> items)
        {
            DataTable dataTable = new DataTable(typeof(T).Name);
            //Get all the properties
            PropertyInfo[] Props = typeof(T).GetProperties(BindingFlags.Public | BindingFlags.Instance);
            foreach (PropertyInfo prop in Props)
            {
                //Setting column names as Property names
                dataTable.Columns.Add(prop.Name);
            }
            foreach (T item in items)
            {
                var values = new object[Props.Length];
                for (int i = 0; i < Props.Length; i++)
                {
                    //inserting property values to datatable rows
                    values[i] = Props[i].GetValue(item, null);
                }
                dataTable.Rows.Add(values);
            }
            //put a breakpoint here and check datatable
            return dataTable;
        }


        #endregion
    }
}
