using CR_API.Models;
using System;
using System.Collections.Generic;
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
            using (QAOrgDBContext dbContext = new QAOrgDBContext())
            {
                return dbContext.Ticket.ToList();
            }
        }

        [Route("api/tickets/get/{id}")]
        [HttpGet]
        public Ticket Get(int id)
        {
            using (QAOrgDBContext dbContext = new QAOrgDBContext())
            {
                return dbContext.Ticket.FirstOrDefault(e => e.TicketID == id);
            }
        }

        [Route("api/tickets/BuildTicket/{buildid}")]
        [HttpGet]
        public IEnumerable<Ticket> BuildTicket(int buildid)
        {
            using(QAOrgDBContext dBContext = new QAOrgDBContext())
            {
                List<BuildTickets> buildTickets= dBContext.BuildTickets.Where(x=> x.BuildID == buildid).ToList();
                List<Ticket> ticketList= new List<Ticket>();

                if (buildTickets.Count > 0)
                {
                    foreach (var item in buildTickets)
                    {
                        ticketList.Add(Get(item.TicketID));
                    }
                }

                return ticketList;
            }
        }

    }
}
