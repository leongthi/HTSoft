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
using System.Web.Http;


namespace CR_API.Controllers
{
    public class TicketsController : ApiController
    {
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
                string Sess = "16FC6B61-3D5D-4DC5-8FBD-013FC42802C9";
                tickets = dBContext.ws_Build_Ticket_InBuild_Get(Sess, buildid, 0).ToList();

                return tickets;
            }
        }


    }
}
